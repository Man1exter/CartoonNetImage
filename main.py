import sys
import requests
from PySide6 import QtWidgets, QtGui, QtCore

class WeatherApp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle(" 🌤 Weather Location App 🌤 ")
        self.setGeometry(800, 400, 400, 125)
        self.init_ui()

    def init_ui(self):
        self.location_input = QtWidgets.QLineEdit(self)
        self.get_weather_button = QtWidgets.QPushButton("Get Weather 🌞", self)
        self.get_weather_button.clicked.connect(self.get_weather_data)
        self.location_maps = QtWidgets.QPushButton("Location Map ⚡", self)
        self.location_maps.clicked.connect(self.loc_map)
        self.clear_button = QtWidgets.QPushButton("Clear 🌊", self)
        self.clear_button.clicked.connect(self.clear)
        self.quit_button = QtWidgets.QPushButton("Quit 🧤", self)
        self.quit_button.clicked.connect(self.quit)
        
        self.location_input.setStyleSheet("background-color: black; color: white; border: 3px solid red; font-size: 20px; font-weight: bold;")
        self.location_maps.setStyleSheet("background-color: orange; color: black; border: 3px solid red; font-size: 20px; font-weight: bold;")
        self.get_weather_button.setStyleSheet("background-color: orange; color: black; border: 3px solid red; font-size: 20px; font-weight: bold;")
        self.clear_button.setStyleSheet("background-color: orange; color: black; border: 3px solid red; font-size: 20px; font-weight: bold;")
        self.quit_button.setStyleSheet("background-color: orange; color: black; border: 3px solid red; font-size: 20px; font-weight: bold;")

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.location_input)
        layout.addWidget(self.get_weather_button)
        layout.addWidget(self.location_maps)
        layout.addWidget(self.clear_button)
        layout.addWidget(self.quit_button)
        self.setLayout(layout)

    def get_weather_data(self,location):
        location = self.location_input.text()
        url = "http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=ea9758fb8307e8eb34c3159485114fec".format(location)
        response = requests.get(url)
        data = response.json()
        
        if "main" in data:
            temperature = data["main"]["temp"]
            weather_description = data["weather"][0]["description"]
            self.show_weather_message(location, temperature, weather_description)
        else:
            QtWidgets.QMessageBox.warning(self, "Error", "Could not retrieve weather data for the given location.")
            
    def show_weather_message(self, location, temperature, weather_description):
        message = "The current weather in {} is {} with a temperature of {:.1f}°C.".format(location, weather_description, temperature)
        QtWidgets.QMessageBox.information(self, "Weather", message)
          
    def loc_map(self):
        location = self.location_input.text()
        url = "https://www.google.com/maps/search/?api=1&query={}".format(location)
        QtGui.QDesktopServices.openUrl(QtCore.QUrl(url))

    def clear(self):
        self.location_input.clear()

    def quit(self):
        QtWidgets.QMessageBox.information(self, "Weather", "See You next time!")
        QtWidgets.QApplication.quit()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    weather_app = WeatherApp()
    weather_app.resize(400, 200)
    weather_app.setStyleSheet("background-color: lightblue;")
    weather_app.show()
    sys.exit(app.exec())
    
    


