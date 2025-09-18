# 🐍 ITS-PYTHON: Comprehensive Python Learning Portfolio

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)

A curated collection of Python projects showcasing my journey from beginner concepts to advanced applications. This repository serves as both a learning portfolio and a practical toolkit, featuring GUI applications, automation scripts, API integrations, and utility tools developed since March 3, 2025.

## 📂 Project Structure

### CRASH/ - Foundational Python Concepts
Learning the basics through practical implementations:
- [`files.py`](CRASH/files.py) - File operations, CSV handling, text processing
- [`HEARTANIMATION.py`](CRASH/HEARTANIMATION.py) - Turtle graphics animation with mathematical curves
- [`main.py`](CRASH/main.py) - Comprehensive collection of basic Python concepts (variables, loops, functions, OOP, encryption, banking system, multithreading, API calls)
- [`POO.py`](CRASH/POO.py) - Object-oriented programming concepts (classes, inheritance, magic methods)

### GUI/ - Graphical User Interface Applications
Exploring different GUI frameworks and their capabilities:
- [`CONFETTI.py`](GUI/CONFETTI.py) - Pygame-based particle animation system
- [`DIGITALCLOCK.py`](GUI/DIGITALCLOCK.py) - PyQt5-based digital clock application
- [`GUI.py`](GUI/GUI.py) - PyQt5 GUI components demonstration (labels, buttons, checkboxes, radio buttons, line edits)
- [`HEART.py`](GUI/HEART.py) - Pygame animated heart drawing with rainbow effects
- [`PARTICLS.py`](GUI/PARTICLS.py) - Pygame particle bloom animation
- [`STOPWATCH.py`](GUI/STOPWATCH.py) - Tkinter-based stopwatch application
- [`WEATHERAPP.py`](GUI/WEATHERAPP.py) - PyQt5 weather application with OpenWeatherMap API integration

### SCRIPTS/ - Utility Scripts and Automation Tools
Command-line tools for various automation and processing tasks:

#### Downloaders
- [`AUDIODOWNLOADER.py`](SCRIPTS/AUDIODOWNLOADER.py) - Audio file downloader
- [`PINTDOWNLOADER.py`](SCRIPTS/PINTDOWNLOADER.py) - Pinterest media downloader
- [`TIKTOKBULKDOWN.py`](SCRIPTS/TIKTOKBULKDOWN.py) - Bulk TikTok video downloader
- [`VIDDOWNLOADER.py`](SCRIPTS/VIDDOWNLOADER.py) - General video downloader
- [`VIDDOWNLOADERBULK.py`](SCRIPTS/VIDDOWNLOADERBULK.py) - Bulk video downloader
- [`YTDOWNLOADER.py`](SCRIPTS/YTDOWNLOADER.py) - YouTube video downloader

#### Converters
- [`DAV2MP4.py`](SCRIPTS/DAV2MP4.py) - DAV to MP4 video converter
- [`DOCXTOEXCELCONVERTER.py`](SCRIPTS/DOCXTOEXCELCONVERTER.py) - Word document to Excel converter
- [`WEBPTOPNG.py`](SCRIPTS/WEBPTOPNG.py) - WebP to PNG image converter

#### Generators
- [`FAKEDATAGENERATOR.PY`](SCRIPTS/FAKEDATAGENERATOR.PY) - Fake data generator using Faker library
- [`PASSWORDGENERATOR.py`](SCRIPTS/PASSWORDGENERATOR.py) - Secure password generator
- [`QRGENERATOR.py`](SCRIPTS/QRGENERATOR.py) - QR code generator

#### Utilities
- [`AUTOPROJECTSETUP.py`](SCRIPTS/AUTOPROJECTSETUP.py) - Automated project setup script
- [`AUTOTHUMBNAIL.py`](SCRIPTS/AUTOTHUMBNAIL.py) - Automatic thumbnail generator
- [`BGREMOVER.py`](SCRIPTS/BGREMOVER.py) - Background removal tool for images
- [`CHATBOT.py`](SCRIPTS/CHATBOT.py) - AI chatbot using Google Gemini
- [`VOICETOTEXT.py`](SCRIPTS/VOICETOTEXT.py) - Voice-to-text conversion
- [`ARAUDOIO2TEXT.py`](SCRIPTS/ARAUDOIO2TEXT.py) - Arabic speech-to-text conversion

## 🛠️ Technologies & Frameworks

### Core Language
- **Python 3.x** - Primary programming language for all applications

### GUI Frameworks
- **PyQt5** - Professional desktop applications (clock, weather app, GUI components)
- **tkinter** - Simple GUI applications (stopwatch)
- **customtkinter** - Modern tkinter wrapper for voice dictation app
- **pygame** - Game-like animations and graphics (confetti, heart, particles)

### Key Libraries
- **speech_recognition** - Google speech-to-text API integration
- **pynput** - Keyboard automation for voice dictation
- **yt-dlp** - Media downloading from various platforms
- **requests** - HTTP requests for API integrations
- **PIL (Pillow)** - Image processing and manipulation
- **faker** - Fake data generation
- **qrcode** - QR code generation
- **rembg** - Background removal from images
- **google-generativeai** - Gemini AI chatbot integration
- **python-dotenv** - Environment variable management
- **tqdm** - Progress bars for downloads
- **turtle** - Simple graphics and animations
- **threading** - Concurrent execution for responsive UIs
- **subprocess** - External command execution (ffmpeg, yt-dlp)

## 🚀 Installation & Setup

### Prerequisites
- Python 3.x installed
- Internet connection for API calls and downloads

### Installation Steps
1. **Clone the repository**
   ```bash
   git clone https://github.com/PURPLE-ORCA/ITS-PYTHON.git
   cd ITS-PYTHON
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Install external tools**
   - Download and install [ffmpeg](https://ffmpeg.org/download.html) for video processing
   - yt-dlp is included in requirements.txt

4. **Configure API keys** (see API Configuration section below)

## 📖 Usage Examples

### Voice Dictation App
Perfect for content creators using Obsidian:
```bash
python EXPORT/DICTATER.py
```
Launch the GUI application and start dictating text directly into your Obsidian notes.

### Weather Application
Get real-time weather information:
```bash
python GUI/WEATHERAPP.py
```
Enter any city name to fetch current weather conditions and forecasts.

### Media Downloader
Download videos from YouTube and other platforms:
```bash
python SCRIPTS/YTDOWNLOADER.py
```
Follow the prompts to enter video URLs and download options.

### Fake Data Generator
Generate realistic test data:
```bash
python SCRIPTS/FAKEDATAGENERATOR.PY
```
Configure fields and generate JSON data for testing purposes.

### QR Code Generator
Create QR codes instantly:
```bash
python SCRIPTS/QRGENERATOR.py
```
Input text or URLs to generate scannable QR codes.

## 🔑 API Configuration

Some applications require API keys for external services. Create a `.env` file in the root directory:

```env
# Google Gemini AI API Key (for chatbot and AI features)
GEMINI_API_KEY=your_google_gemini_api_key_here

# OpenWeatherMap API Key (for weather application)
WEATHER_API_KEY=your_openweathermap_api_key_here
```

### Getting API Keys
- **Google Gemini**: Visit [Google AI Studio](https://makersuite.google.com/app/apikey) to generate an API key
- **OpenWeatherMap**: Sign up at [OpenWeatherMap](https://openweathermap.org/api) for a free API key
---


*Built with ❤️ during my Python learning adventure starting March 3, 2025*