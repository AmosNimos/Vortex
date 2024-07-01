import sys
import requests
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QLineEdit, QToolBar, QAction, QMenu, QMessageBox, QFileDialog
)
from PyQt5.QtWebEngineWidgets import QWebEngineView

default_url = "https://www.wiby.me/surprise"

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl(default_url))

        self.browser.page().urlChanged.connect(self.update_url_bar)
        self.browser.setContextMenuPolicy(Qt.ActionsContextMenu)  # Enable custom context menu

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.main_layout = QVBoxLayout(self.central_widget)
        self.setup_toolbars()

        self.main_layout.addWidget(self.browser, 1)  # Add browser widget with stretch factor

        # Set white text on pure black background
        self.setStyleSheet("background-color: #000000; color: #FFFFFF;")

        self.setWindowTitle("Vortex")
        self.show()

    def setup_toolbars(self):
        self.toolbar_actions = QToolBar()
        self.addToolBar(Qt.TopToolBarArea, self.toolbar_actions)

        self.back_action = QAction("<", self)
        self.back_action.triggered.connect(self.browser.back)
        self.toolbar_actions.addAction(self.back_action)

        self.forward_action = QAction(">", self)
        self.forward_action.triggered.connect(self.browser.forward)
        self.toolbar_actions.addAction(self.forward_action)

        self.reload_action = QAction("⟳", self)
        self.reload_action.triggered.connect(self.browser.reload)
        self.toolbar_actions.addAction(self.reload_action)

        self.save_html_action = QAction("↓", self)
        self.save_html_action.triggered.connect(self.save_page)
        self.toolbar_actions.addAction(self.save_html_action)

        self.toolbar_url = QToolBar()
        self.addToolBar(Qt.TopToolBarArea, self.toolbar_url)

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        self.url_bar.setMinimumWidth(300)  # Set minimum width for the url bar
        self.toolbar_url.addWidget(self.url_bar)

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

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
