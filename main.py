import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget, QLineEdit, QListWidget, QMessageBox
from tailscale_manager import TailscaleManager
from winbox_manager import WinBoxManager

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        
        self.tailscale_manager = TailscaleManager()
        self.winbox_manager = WinBoxManager()

    def initUI(self):
        self.setWindowTitle("Tailscale VPN Manager")
        self.setGeometry(100, 100, 600, 400)
        
        layout = QVBoxLayout()

        self.network_label = QLabel("Tailscale Network Key:")
        layout.addWidget(self.network_label)
        
        self.network_input = QLineEdit(self)
        layout.addWidget(self.network_input)

        self.add_button = QPushButton("Add Tailscale Network", self)
        self.add_button.clicked.connect(self.add_network)
        layout.addWidget(self.add_button)

        self.networks_list = QListWidget(self)
        layout.addWidget(self.networks_list)

        self.connect_button = QPushButton("Connect Selected Network", self)
        self.connect_button.clicked.connect(self.connect_network)
        layout.addWidget(self.connect_button)

        self.launch_winbox_button = QPushButton("Launch WinBox", self)
        self.launch_winbox_button.clicked.connect(self.launch_winbox)
        layout.addWidget(self.launch_winbox_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def add_network(self):
        network_key = self.network_input.text()
        if network_key:
            self.tailscale_manager.add_network(network_key)
            self.networks_list.addItem(network_key)
            self.network_input.clear()
        else:
            QMessageBox.warning(self, "Input Error", "Please enter a valid Tailscale network key.")

    def connect_network(self):
        selected_item = self.networks_list.currentItem()
        if selected_item:
            network_key = selected_item.text()
            self.tailscale_manager.connect_network(network_key)
        else:
            QMessageBox.warning(self, "Selection Error", "Please select a network to connect.")

    def launch_winbox(self):
        selected_item = self.networks_list.currentItem()
        if selected_item:
            network_key = selected_item.text()
            self.winbox_manager.launch_winbox(network_key)
        else:
            QMessageBox.warning(self, "Selection Error", "Please select a network to manage with WinBox.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
