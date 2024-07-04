# <img src="icon.png" width="64px" height="64px"> V0rtex Br0wser 

## Introduction

Welcome to **V0rtex**, Just trying to be a functional minimal python web browser! V0rtex is an open-source browser designed with hobbyists and Linux users in mind.

**V0rtex** : Use It, Hack It, Own It

> Navigate the Information Superhighway (Internet) Without Built-in Influence or Interference from Large Monopolies and Political Agendas. A Step Towards a Free Digital Frontier!

## Philosophy and Vision
Amidst a landscape dominated by corporate giants, V0rtex emerges as a minimalist alternative. Rooted in the libre software movement, V0rtex empowers users with an accessible, comprehensible browser experience, distinct from Chromium-based norms. It stands for user choice and independence, offering a soulful alternative in today's tech sphere.

I don't claim that this browser is innovative; it doesn't need to be. This is about reinventing the wheel in a way that aligns with a different set of values. V0rtex is designed to be small and minimal, focusing on simplicity and user control. It's not about breaking new ground but about providing an alternative that improves over time.

V0rtex is, above all, an idea—a vision to provide more alternatives to combat the big-tech monopoly and influence over the browser market. If you find the project too simple, then create your own! If it doesn't meet your needs, contribute and help shape a version that does. The core need I'm addressing is the lack of alternatives.

V0rtex's primary task is simply to work at accessing the web. V0rtex is aiming to offer the minimum needed to access the web.

## Values
- **Clarity**: The browser aims to offer a clean and straightforward user interface, making it easy for users to navigate and use the features without unnecessary complexity.

- **Transparency**: V0rtex is open-source and provides users with insight into how it works. This openness ensures users can trust the software and understand what it does, promoting an honest and clear relationship between the software and its users.

- **Deep Customization**: The browser aim to be highly customizable, allowing users to modify and tailor the browser to their specific needs and preferences. This includes changing the appearance, behavior, and functionalities to suit individual workflows and styles.

### What it is not
- A **Modern** browser
- Privacy/Safety focused (I am not specialized enough to make any claims about its privacy or safety. There are already many browsers that focus on these aspects; this is just not one of them. I mainly use defaults.)

## Screenshots
<img src="vortex_Screenshot_2024-07-02 12-11-18.png">

## Basic functionality

### Customizable GUI
- **Move GUI Elements**: Arrange and position toolbar buttons, URL bars, and other interface components to suit your workflow.
- **Theme Customization**: Easily change the color, text size, and style of the entire application.

### Web Page Customization
- **Automatic CSS Injection**: Write and apply your custom CSS to any webpage you visit, modifying the look and feel to your preferences. This allows for easy and direct customization without the need for complex setups or extensions.
- **Automatic JavaScript Injection**: Inject custom JavaScript into webpages to enhance functionality or automate tasks. Unlike many modern browsers that require compiling extensions or writing manifests, V0rtex allows you to simply paste your scripts into a `script.js` file, and they will run automatically. This straightforward approach makes it easy to customize and extend the browser’s capabilities.

#### Default Browser Features

- Favorites: Easily save and load your favorite websites url to a text file for quick access.
- Script and CSS Control: Disable scripts and CSS on webpages to enhance security and reduce unnecessary content.

#### Simplicity and Minimalism
- **Minimalist Design**: V0rtex focuses on providing a clean and straightforward browsing experience without unnecessary clutter.

- **Rich Feature Set**: Despite its simplicity, V0rtex attempts to offer all the **essential** features you expect from a minimal browser.

- **Portable and Lightweight**: The main V0rtex browser code is designed as a single file (excluding minimal library requirements), ensuring ease of distribution and setup.

- **Minimalism at its Core**: V0rtex embodies the philosophy of minimalism, offering a highly customizable browsing experience with minimal overhead. By maintaining a single-file core and minimal dependencies, V0rtex streamlines both user experience and development.

- **Following the Unix Philosophy**: V0rtex adheres to the Unix philosophy of doing one thing and doing it well—providing a reliable web browsing experience. This approach focuses on delivering efficiency and robust functionality without unnecessary complexity.

🚧 Disclaimer: This project is still in development. 🚧 Not all features might be fully implemented yet or may be missing entirely.

## Why Open Source?

V0rtex could have been just another closed-source project hidden in the shadows, but I chose to share it with the world! It had to be open source to truly fulfill its potential as one of the most hackable, modifiable, and customizable browsers available. By using Python, a beginner-friendly programming language, V0rtex becomes even more accessible and customizable.

Feel free to create your own branch or fork of this project. Just make sure to link back to the original repository and provide proper accreditation on the main page, both for recognition and license compliance.

Being open source allows V0rtex to be truly customizable. Users can modify the source code to add new features, fix bugs, or enhance existing functionality. Contributions from the community help to make V0rtex "THE" world's most customizable browser.

### Installation

To install V0rtex on your Linux system, follow these steps:

1. **Copy the source code:**
   Simply copy the entire content of the `v0rtex.py` file from the repository.

2. **Paste the code into a new file:**
   Create a new file on your system and paste the copied code into it. Save the file as `v0rtex.py`.

3. **Install the necessary dependencies:**
   Ensure you have Python installed. Then, install the required libraries:
   ```bash
   pip install requests PyQt5
   ```

4. **Run the application:**
   ```bash
   python v0rtex.py
   ```

### For Users Wanting to Customize the Source Code

The project will always have a <a href="https://github.com/AmosNimos/Vortex/releases">release</a> available for Linux. However, these steps are for users wanting to customize the source code, not just the compiled release. Keep in mind one of the principles of V0rtex is to keep the project as a single file so people can simply copy the code into their clipboard and paste it into an empty file to get the full project on their computer! As long as they have Python and the required libraries installed, they can run V0rtex. Therefore, you don't really have a reason to clone the whole repository unless you want to create a fork or contribute to the original project.

### Forking the Project

1. **Fork the repository on GitHub:**
   Go to the V0rtex repository on GitHub and click the "Fork" button in the upper-right corner of the page.

2. **Clone your fork:**
   ```bash
   git clone https://github.com/yourusername/v0rtex.git
   ```

3. **Navigate to the project directory:**
   ```bash
   cd v0rtex
   ```

4. **Create a new branch for your changes:**
   ```bash
   git checkout -b my-new-feature
   ```

5. **Make your changes and commit them:**
   ```bash
   git add .
   git commit -m "Add some feature"
   ```

6. **Push your changes to your fork:**
   ```bash
   git push origin my-new-feature
   ```

### Suggesting a Contribution

1. **Create a pull request:**
   After pushing your changes to your fork, go to the original V0rtex repository and create a new pull request. Be sure to describe your changes and why they should be merged.

2. **Wait for review:**
   The project maintainers will review your pull request and provide feedback or merge it into the main project.

> NOTE: The libraries are not included in the repository but can be installed using the `requirements.txt` file provided.

By following these instructions, you can easily customize and contribute to the V0rtex project, ensuring that it remains one of the most hackable and customizable browsers available.

### Configuration
V0rtex uses a configuration file located at `~/.config/v0rtex/v0rtex.conf`. This file allows you to set default settings such as the default URL, background color, foreground color, font size, and toggles for JavaScript, CSS, and cookies.

To ensure the configuration file and necessary directories are set up, run the following script:
```python
python setup_config.py
```

### Main Libraries Used in the V0rtex Project

1. **sys**
2. **requests**
3. **PyQt5.QtCore (Qt, QUrl)**
4. **pathlib (Path)**
5. **configparser**
6. **PyQt5.QtWidgets (QApplication, QMainWindow, QWidget, QVBoxLayout, QLineEdit, QToolBar, QAction, QMenu, QMessageBox, QFileDialog, QTextEdit, QToolButton)**
7. **PyQt5.QtWebEngineWidgets (QWebEngineView, QWebEngineSettings)**

>  ⚠️ Disclaimer: This list can be outdated. Look at the top of the `vortex.py` file for a current, up-to-date library list.

## Contributing
We welcome contributions from the community! If you have ideas for new features, bug fixes, or enhancements, feel free to submit a pull request on our [GitHub repository](https://github.com/AmosNimos/Vortex).

## License
V0rtex is licensed under the GNU AGPL License. See the [LICENSE](LICENSE) file for more details.

## Conclusion

V0rtex aims to be a highly customizable and hackable browser designed for Linux users and hobbyists who appreciate simplicity and intuitive customization. Its minimalist approach ensures a sleek and efficient browsing experience. Download V0rtex today to personalize your browsing environment and make it truly yours!

---

> ⚠️ Disclaimer: I use ChatGPT to check spelling and rephrase my README, and to help me in crafting this browser. Contributors should feel free to use AI tools too, as it's the result that matters. I know AI does not replace hard work when used correctly to enhance a project.

Feel free to reach out with any questions or suggestions. Happy browsing with V0rtex!

> Created by Amosnimos 2024 - Under GNU AGPL License
