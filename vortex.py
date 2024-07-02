import sys
import requests
import configparser
from pathlib import Path
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtGui import QIcon, QPixmap, QPainter
#import QtWidgets
from PyQt5.QtWidgets import (
    QScrollBar, QInputDialog, QSizePolicy, QDialogButtonBox, QPushButton, QListWidget, QListWidgetItem, QDialog, QApplication, QMainWindow, QWidget, QVBoxLayout, QLineEdit, QToolBar, QToolButton,
    QLabel, QMessageBox, QFileDialog, QTextEdit, QMenu
)
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineSettings

gui_fg="#000000"
gui_bg="#FFFFFF"
css_toggle="True"
js_toggle="true"
cookie_toggle="true"

        
class FavoritesDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Favorites")

        # Load favorite URLs from file
        fav_file = Path.home() / '.config' / 'vortex' / 'fav.txt'
        self.favorite_urls = []
        if fav_file.exists():
            with open(fav_file, 'r') as f:
                self.favorite_urls = f.read().splitlines()

        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout(self)
        self.list_widget = QListWidget(self)

        # Add favorite URLs to list widget
        for url in self.favorite_urls:
            item = QListWidgetItem(url)
            self.list_widget.addItem(item)

        layout.addWidget(self.list_widget)

        # Add button to set selected URL as default and close dialog
        self.button_set_default = QPushButton("O")
        self.button_set_default.clicked.connect(self.set_default_and_close)
        self.button_set_default.setStyleSheet(self.button_stylesheet())

        # Add button to add current URL to favorites and close dialog
        self.button_add_to_favorites = QPushButton("+")
        self.button_add_to_favorites.clicked.connect(self.add_to_favorites)
        self.button_add_to_favorites.setStyleSheet(self.button_stylesheet())
        
        # Add Cancel button
        self.button_cancel = QPushButton("✕")
        self.button_cancel.clicked.connect(self.cancel_dialog)
        self.button_cancel.setStyleSheet(self.button_stylesheet())

        # Add buttons to a button box for better layout
        button_box = QDialogButtonBox()
        button_box.addButton(self.button_add_to_favorites, QDialogButtonBox.AcceptRole)
        button_box.addButton(self.button_set_default, QDialogButtonBox.AcceptRole)
        button_box.addButton(self.button_cancel, QDialogButtonBox.RejectRole)


        layout.addWidget(button_box)

    def set_default_and_close(self):
        selected_items = self.list_widget.selectedItems()
        if selected_items:
            selected_url = selected_items[0].text()
            # Set selected URL as default_url in main window
            main_window = self.parent()
            if hasattr(main_window, 'url_bar'):
                main_window.url_bar.setText(selected_url)
                main_window.navigate_to_url()
                self.accept()  # Close the dialog
            else:
                QMessageBox.warning(self, "Error", "URL bar not found in main window")

#    def add_to_favorites(self):
#        # Get the main window instance
#        main_window = self.parent()
#        if main_window is None:
#            return
#        
#        # Get the current URL from the main window
#        current_url = main_window.browser.url().toString()
#
#        # Save the current URL to favorites file
#        fav_file = Path.home() / '.config' / 'vortex' / 'fav.txt'
#        try:
#            with open(fav_file, 'a') as f:
#                f.write(current_url + '\n')
#            QMessageBox.information(self, "Success", "URL added to favorites.")
#        except Exception as e:
#            QMessageBox.critical(self, "Error", f"Failed to add URL to favorites: {str(e)}")
#        self.reject()  # Close the dialog

    def add_to_favorites(self):
        # Get the main window instance
        main_window = self.parent()
        if main_window is None:
            return

        # Get the current URL from the main window
        current_url = main_window.browser.url().toString()

        # Check if the URL is already in favorites
        fav_file = Path.home() / '.config' / 'vortex' / 'fav.txt'
        if current_url in open(fav_file).read():
            QMessageBox.warning(self, "Already in Favorites", "This URL is already in your favorites.")
            self.reject()  # Close the dialog without adding duplicate
            return

        # Save the current URL to favorites file
        try:
            with open(fav_file, 'a') as f:
                f.write(current_url + '\n')
            QMessageBox.information(self, "Success", "URL added to favorites successfully.")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to add URL to favorites: {str(e)}")

        self.reject()  # Close the dialog after adding or handling the error

    def cancel_dialog(self):
        self.reject()  # Close the dialog without making any changes
        
    def button_stylesheet(self,):
        return f"""
            QPushButton {{
                background-color: {gui_bg};
                border: 2px solid {gui_fg};
                color: {gui_fg};
                padding: 2px;
                margin: 2px;
            }}
            QPushButton:hover {{
                background-color: {gui_fg};
                color: {gui_bg};
            }}
        """
        #self.setup_ui = QLineEdit()
        #self.setup_ui.returnPressed.connect(self.navigate_to_url)
        #self.setup_ui.setMinimumWidth(400)  # Set minimum width for the url bar
# ---            

                
def str_to_bool(s):
    return s.lower() == 'true'
    
def ensure_vortex_config():
    # Define the Vortex directory and files
    home_dir = Path.home()
    config_dir = home_dir / '.config' / 'vortex'
    config_file = config_dir / 'vortex.conf'
    other_files = ['fav.txt', 'style.css', 'theme.css']

    # Create the directory if it doesn't exist
    if not config_dir.exists():
        config_dir.mkdir(parents=True)
        print(f"Created directory: {config_dir}")

    # Create the vortex.conf file with default settings if it doesn't exist
    if not config_file.exists():
        config = configparser.ConfigParser()
        config['Settings'] = {
            'default_url': '',
            'bg': '#000000',
            'fg': '#FFFFFF',
            'size': '18',
            'js': 'true',
            'css': 'True',
            'cookie': 'true'
        }
        with open(config_file, 'w') as f:
            config.write(f)
        print(f"Created file with default settings: {config_file}")
    else:
        print(f"Config file already exists: {config_file}")

    # Create the other files if they don't exist
    for file_name in other_files:
        file_path = config_dir / file_name
        if not file_path.exists():
            file_path.touch()
            print(f"Created file: {file_path}")

def read_vortex_config():
    config_file = Path.home() / '.config' / 'vortex' / 'vortex.conf'
    config = configparser.ConfigParser()

    if config_file.exists():
        config.read(config_file)
        print(f"Read configuration from: {config_file}")
    else:
        raise FileNotFoundError(f"{config_file} does not exist")

    # Ensure the Settings section exists
    if 'Settings' not in config:
        raise KeyError("The 'Settings' section is missing in the configuration file")

    # Check if default_url is empty, set it to default_url if so
    if config['Settings'].get('default_url') == "":
        default_url = "www.wiby.me/surprise"  # Your default URL
        config['Settings']['default_url'] = default_url

    return config['Settings']


class MainWindow(QMainWindow):
    def __init__(self, default_url, gui_size):
        super().__init__()

        self.setWindowTitle("Vortex")

                      
        # Load PNG file
        icon_path = 'icon.png'  # Adjust path as per your project structure
        pixmap = QPixmap(icon_path)
        
        # Set window icon
        self.setWindowIcon(QIcon(pixmap))


        # Example label with PNG content
        label = QLabel(self)
        label.setGeometry(10, 10, 64, 64)  # Adjust size and position
        label.setPixmap(pixmap)
        
        self.browser = QWebEngineView()
        if not default_url.startswith(('http://', 'https://')):
            default_url = 'http://' + default_url

        self.browser.setUrl(QUrl(default_url))
        self.browser.loadFinished.connect(self.apply_settings)

        # Toggle CSS for web pages
        settings = QWebEngineSettings.globalSettings()

        self.browser.page().urlChanged.connect(self.update_url_bar)
        self.browser.setContextMenuPolicy(Qt.ActionsContextMenu)  # Enable custom context menu

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.main_layout = QVBoxLayout(self.central_widget)
        self.setup_toolbars()
        #self.default_url = default_url

        self.main_layout.addWidget(self.browser, 1)  # Add browser widget with stretch factor

        # Set white text on pure black background
        self.setStyleSheet("background-color: "+str(gui_bg)+"; color: "+str(gui_fg)+"; font-size: "+str(gui_size)+"px;")

        self.setWindowTitle("Vortex")
        self.show()

    def setup_toolbars(self):
        # Main actions toolbar
        self.toolbar_actions = QToolBar()
        self.addToolBar(Qt.TopToolBarArea, self.toolbar_actions)


        # Create a menu to hold toolbar actions
        self.toolbar_menu = QMenu(self)

        # Back button
        self.back_button = QToolButton()
        self.back_button.setText("<")
        self.back_button.setToolTip("Back")
        self.back_button.clicked.connect(self.browser.back)
        self.toolbar_actions.addWidget(self.back_button)

        self.forward_button = QToolButton()
        self.forward_button.setText(">")
        self.forward_button.setToolTip("Forward")
        self.forward_button.clicked.connect(self.browser.forward)
        self.toolbar_actions.addWidget(self.forward_button)

        self.reload_button = QToolButton()
        self.reload_button.setText("⟳")
        self.reload_button.setToolTip("Reload")
        self.reload_button.clicked.connect(self.browser.reload)
        self.toolbar_actions.addWidget(self.reload_button)

        self.save_button = QToolButton()
        self.save_button.setText("↓")
        self.save_button.setToolTip("Save HTML")
        self.save_button.clicked.connect(self.save_page)
        self.toolbar_actions.addWidget(self.save_button)

        # Favorite button
        self.favorite_button = QToolButton()
        self.favorite_button.setText("+")
        self.favorite_button.setToolTip("Add to Favorites")
        self.favorite_button.clicked.connect(self.add_to_favorites)
        self.toolbar_actions.addWidget(self.favorite_button)

        # URL toolbar
        self.toolbar_url = QToolBar()
        self.addToolBar(Qt.TopToolBarArea, self.toolbar_url)

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        self.url_bar.setMinimumWidth(300)  # Set minimum width for the url bar
        self.toolbar_url.addWidget(self.url_bar)

        # New favorites button
        self.favorites_button = QToolButton()
        self.favorites_button.setText("★")
        self.favorites_button.setToolTip("View Favorites")
        self.favorites_button.clicked.connect(self.show_favorites)
        self.toolbar_actions.addWidget(self.favorites_button)

        self.favorites_button.setStyleSheet(self.button_stylesheet())
        self.favorite_button.setStyleSheet(self.button_stylesheet())
        self.back_button.setStyleSheet(self.button_stylesheet())
        self.forward_button.setStyleSheet(self.button_stylesheet())
        self.reload_button.setStyleSheet(self.button_stylesheet())
        self.save_button.setStyleSheet(self.button_stylesheet())

#    def show_favorites(self):
#        # Implement this method to show the list of favorites
#        favorites_dialog = FavoritesDialog(self)
#        favorites_dialog.exec_()

    def show_favorites(self):
        # Implement this method to show the list of favorites
        favorites_dialog = FavoritesDialog(self)
        favorites_dialog.exec_()

        # Set hover effects using style sheet


        # Associate the menu with the dropdown button
#        self.dropdown_button.setMenu(self.toolbar_menu)
#        self.dropdown_button.setPopupMode(QToolButton.MenuButtonPopup)

    def add_to_favorites(self):
        url = self.browser.url().toString()
        fav_file = Path.home() / '.config' / 'vortex' / 'fav.txt'

        try:
            with open(fav_file, 'a') as f:
                f.write(url + '\n')
            QMessageBox.information(self, "Success", "URL added to favorites.")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to add URL to favorites: {str(e)}")

    def button_stylesheet(self,):
        return f"""
            QToolButton {{
                background-color: {gui_bg};
                border: 2px solid {gui_fg};
                color: {gui_fg};
                padding: 2px;
                margin: 2px;
            }}
            QToolButton:hover {{
                background-color: {gui_fg};
                color: {gui_bg};
            }}
        """
        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        self.url_bar.setMinimumWidth(400)  # Set minimum width for the url bar
        self.toolbar_url.addWidget(self.url_bar)

    def apply_settings(self):
#        if not css_toggle:
            # Disable CSS before the page is loaded
#            settings = self.browser.page().settings()
#            settings.setAttribute(QWebEngineSettings.JavascriptEnabled, False)
#            settings.setAttribute(QWebEngineSettings.AutoLoadImages, False)
#            settings.setAttribute(QWebEngineSettings.PluginsEnabled, False)

       # Disable native scroll bars and inject custom CSS
        #settings = QWebEngineSettings.globalSettings()
        #settings.setAttribute(QWebEngineSettings.ScrollBarDragEnabled, False)
        #settings.setAttribute(QWebEngineSettings.ScrollBarContextMenuEnabled, False)

        if not css_toggle:
            settings = self.browser.page().settings()
            settings.setAttribute(QWebEngineSettings.AutoLoadImages, False)
            # Inject custom CSS to disable all styles on the page
            print("css off")
            disable_css_script = """
            var styleElement = document.createElement('style');
            styleElement.textContent = '* { all: unset !important; }';
            document.head.appendChild(styleElement);
            """
            self.browser.page().runJavaScript(disable_css_script)
                        
    def navigate_to_url(self):
        url = self.url_bar.text()
        if not url.startswith("http"):
            url = "http://" + url
        self.browser.setUrl(QUrl(url))

    def update_url_bar(self, q):
        self.url_bar.setText(q.toString())

    def contextMenuEvent(self, event):
        menu = QMenu(self)

        view_source_action = menu.addAction("View Page Source")
        view_source_action.triggered.connect(self.view_page_source)

        menu.exec_(event.globalPos())

    def view_page_source(self):
        self.browser.page().toHtml(lambda html: self.show_page_source(html))

    def show_page_source(self, html):
        dialog = QMessageBox()
        dialog.setWindowTitle("Page Source")
        text_edit = QTextEdit()
        text_edit.setPlainText(html)
        dialog.layout().addWidget(text_edit)
        dialog.exec_()

    def save_page(self):
        file_dialog = QFileDialog(self)
        file_dialog.setFileMode(QFileDialog.AnyFile)
        file_dialog.setAcceptMode(QFileDialog.AcceptSave)
        file_dialog.setNameFilter("HTML Files (*.html)")

        if file_dialog.exec_():
            file_path = file_dialog.selectedFiles()[0]
            url = self.browser.url().toString()

            try:
                response = requests.get(url)
                if response.status_code == 200:
                    html_content = response.text
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(html_content)
                    QMessageBox.information(self, "Success", f"Page saved to {file_path}")
                else:
                    QMessageBox.warning(self, "Error", f"Failed to fetch page content from {url}")
            except requests.RequestException as e:
                QMessageBox.critical(self, "Error", f"Error fetching page content: {str(e)}")

def main():
    # config
    ensure_vortex_config()
    try:
        settings = read_vortex_config()
    except KeyError as e:
        print(f"Error: {e}")
        return
    
    default_url = settings.get('default_url')
    global gui_fg, gui_bg, css_toggle
    gui_bg = settings.get('bg')
    gui_fg = settings.get('fg')
    gui_size = settings.get('size')
    js_toggle = settings.get('js')
    css_toggle = str_to_bool(settings.get('css'))
    cookie_toggle = settings.get('cookie_toggle')
    app = QApplication(sys.argv)
    window = MainWindow(default_url,gui_size)
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
