# Weather Station Dashboard
A Raspberry Pi-based weather monitoring system with web interface.
## Project Overview
This project reads temperature and humidity data from a DHT sensor and displays
it on a web dashboard with configurable alerts. Visual (LED) and audio (buzzer)
alerts notify users when thresholds are exceeded.
## Hardware Requirements
- Raspberry Pi 5
- DHT11 or DHT22 Temperature/Humidity Sensor
- RGB LED or 3 individual LEDs (Red, Green, Blue)
- Active Buzzer
- Resistors (220Ω for LEDs)
- Breadboard and jumper wires
## Software Stack
- Python 3.11+
- Flask (Web framework)
- GPIO control libraries
- HTML/CSS/JavaScript (Frontend)
## Setup Instructions
1. Clone this repository
2. Create a virtual environment: `python3 -m venv venv`
3. Activate virtual environment: `source venv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt` (coming soon)
5. Run the application: `python3 app.py` (coming soon)
## Configuration
Edit `config/settings.py` to adjust:
- GPIO pin assignments
- Sensor read intervals
- Temperature and humidity thresholds
- Flask server settings
## Author
[Your Name]
## Date Started
January 10, 2026
## Project Status
Day 2: Git version control implementation
