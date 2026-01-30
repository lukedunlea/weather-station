#=========================================================================#

# Weather Station & Distributed Hardware Dashboard

A Raspberry Pi–based distributed hardware project that reads live temperature data and shares it across devices using REST APIs and web dashboards.

---

## Project Overview

This project is a distributed IoT-style system built using two Raspberry Pis on the same local network.

- One Raspberry Pi acts as a **temperature sensor server**, reading live temperature data from a thermistor via an ADC and exposing it through a Flask API.
- A second Raspberry Pi acts as an **RGB LED controller**, reacting automatically to the temperature data and displaying its state through a separate web interface.
- Both devices host web dashboards that show live data by communicating with each other using HTTP requests.

The project demonstrates real-world concepts such as API design, inter-device communication, browser-based dashboards, and hardware control.

---

## System Architecture

- **Temperature Pi**
  - Reads temperature from a thermistor sensor
  - Exposes `/api/sensor` endpoint
  - Hosts a web dashboard showing live temperature and LED status

- **RGB LED Pi**
  - Controls an RGB LED using GPIO
  - Exposes `/api/color`, `/api/status`, and `/api/toggle` endpoints
  - Runs a client script that fetches temperature data and sets LED colour automatically
  - Hosts a web dashboard showing LED controls and live temperature from the other Pi

Both devices communicate over the local network using IP addresses.

---

## Hardware Requirements

### Temperature Server
- Raspberry Pi 5
- Thermistor
- ADC module (PCF8591 or ADS7830)
- Resistors
- Breadboard and jumper wires

### RGB Controller
- Raspberry Pi 5
- RGB LED (common anode)
- Resistors (220Ω)
- Breadboard and jumper wires

---

## Software Stack

- Python 3
- Flask (web server and APIs)
- Flask-CORS (cross-origin browser access)
- requests (Python HTTP client)
- HTML / CSS / JavaScript (frontend dashboards)
- GPIO libraries for Raspberry Pi

---

## Features

- Live temperature readings
- Automatic LED colour changes based on temperature thresholds
- Web dashboards on both devices
- Cross-device communication using REST APIs
- Real-time updates without page refresh
- Clean separation between hardware control, APIs, and frontend logic

---

## Configuration Note

This project runs across two Raspberry Pis on the same local network.
Before running the project, replace the IP addresses with
the correct local IPs for your setup.

Example:
- TEMPERATURE_PI_IP → 192.168.1.50
- RGB_PI_IP → 192.168.1.51

### 1. Clone the repository
```bash
git clone https://github.com/lukedunlea/weather_station.git
cd weather_station

