import sys
import requests
from PySide6 import QtWidgets, QtGui

class WeatherApp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(" 🌤 Weather Location App 🌤 ")
        self.setGeometry(800, 400, 400, 125)
        self.init_ui()

    def init_ui(self):
        self.location_input = QtWidgets.QLineEdit(self)
        self.get_weather_button = QtWidgets.QPushButton("Get Weather 🌞", self)
        self.get_weather_button.clicked.connect(self.get_weather)
        self.clear_button = QtWidgets.QPushButton("Clear 🌊", self)
        self.clear_button.clicked.connect(self.clear)
        self.quit_button = QtWidgets.QPushButton("Quit 🧤", self)
        self.quit_button.clicked.connect(self.quit)
        
        self.location_input.setStyleSheet("background-color: black; color: white; border: 3px solid red; font-size: 20px; font-weight: bold;")
        self.get_weather_button.setStyleSheet("background-color: orange; color: black; border: 3px solid red; font-size: 15px; font-weight: bold;")
        self.clear_button.setStyleSheet("background-color: orange; color: black; border: 3px solid red; font-size: 15px; font-weight: bold;")
        self.quit_button.setStyleSheet("background-color: orange; color: black; border: 3px solid red; font-size: 15px; font-weight: bold;")

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.location_input)
        layout.addWidget(self.get_weather_button)
        layout.addWidget(self.clear_button)
        layout.addWidget(self.quit_button)
        self.setLayout(layout)

    def get_weather(self):
        location = self.location_input.text()
        QtWidgets.QMessageBox.information(self, "Weather", "The current weather in {} is: {}".format(location, "weather"))

    def clear(self):
        self.location_input.clear()

    def quit(self):
        QtWidgets.QApplication.quit()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    weather_app = WeatherApp()
    weather_app.resize(400, 200)
    weather_app.setStyleSheet("background-color: lightgreen;")
    weather_app.show()
    sys.exit(app.exec())
    
    


