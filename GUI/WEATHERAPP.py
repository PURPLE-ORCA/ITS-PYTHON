import sys
import requests
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox
)
from PyQt5.QtGui import QFont, QPalette, QColor
from PyQt5.QtCore import Qt
from dotenv import load_dotenv
import os

dotenv_path = os.path.join(os.path.dirname(__file__), ".env")
load_dotenv(dotenv_path)
API_KEY = os.getenv("WEATHER_API_KEY")

class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()

        # Window settings
        self.setWindowTitle("Weather App ☀️")
        self.setGeometry(100, 100, 350, 250)
        self.setStyleSheet("background-color: #2E2E2E; border-radius: 10px;")

        # Fonts
        label_font = QFont("Arial", 12, QFont.Bold)
        weather_font = QFont("Arial", 26, QFont.Bold)

        # Widgets
        self.city_label = QLabel("Enter city name:")
        self.city_label.setFont(label_font)
        self.city_label.setStyleSheet("color: #FFFFFF;")

        self.city_input = QLineEdit()
        self.city_input.setFont(label_font)
        self.city_input.setStyleSheet(
            "background-color: #444; color: #FFF; border-radius: 8px; padding: 6px;"
        )

        self.get_weather_button = QPushButton("Get Weather 🌤️")
        self.get_weather_button.setFont(label_font)
        self.get_weather_button.setStyleSheet(
            "background-color: #4CAF50; color: white; border-radius: 8px; padding: 6px;"
        )

        self.temperature_label = QLabel("Temperature: -°C")
        self.temperature_label.setFont(weather_font)
        self.temperature_label.setStyleSheet("color: #FFD700;")  # Gold color

        self.description_label = QLabel("Condition: -")
        self.description_label.setFont(weather_font)
        self.description_label.setStyleSheet("color: #87CEEB;")  # Light blue

        # Layout
        layout = QVBoxLayout()
        layout.setSpacing(12)
        layout.addWidget(self.city_label, alignment=Qt.AlignCenter)
        layout.addWidget(self.city_input, alignment=Qt.AlignCenter)
        layout.addWidget(self.get_weather_button, alignment=Qt.AlignCenter)
        layout.addWidget(self.temperature_label, alignment=Qt.AlignCenter)
        layout.addWidget(self.description_label, alignment=Qt.AlignCenter)
        self.setLayout(layout)

        # Button action
        self.get_weather_button.clicked.connect(self.get_weather)

    def get_weather(self):
        city = self.city_input.text().strip()
        if not city:
            QMessageBox.warning(self, "Input Error", "Please enter a city name.")
            return

        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

        try:
            response = requests.get(url)
            data = response.json()

            print("API Response:", data)  # Debugging line

            if response.status_code == 200:
                temp = data["main"]["temp"]
                condition = data["weather"][0]["description"].capitalize()
                self.temperature_label.setText(f"Temperature: {temp}°C")
                self.description_label.setText(f"Condition: {condition}")
            else:
                QMessageBox.warning(self, "Error", f"City not found: {city}")

        except requests.exceptions.RequestException as e:
            QMessageBox.critical(self, "Network Error", f"Failed to fetch data: {e}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    weather_app = WeatherApp()
    weather_app.show()
    sys.exit(app.exec_())
