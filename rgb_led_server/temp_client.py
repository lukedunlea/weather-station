import time
import requests

# -------- CONFIG --------
# Your Pi (temperature provider)
TEMP_API_URL = "http://192.168.68.72:5000/api/sensor"

# Sam's Pi (RGB controller)
RGB_API_URL = "http://127.0.0.1:5000/api/color"

# -------- HELPERS --------
def get_temperature():
    response = requests.get(TEMP_API_URL, timeout=2)
    response.raise_for_status()
    data = response.json()
    return data["temperature"]

def set_rgb_color(r, g, b):
    payload = {"color": [int(r), int(g), int(b)]}
    requests.post(RGB_API_URL, json=payload, timeout=2)


# -------- MAIN LOOP --------
if __name__ == "__main__":
    print("Temp client started. Reading temperature and controlling RGB LED...")

    while True:
        try:
            temp = get_temperature()
            print(f"Current temperature: {temp} °C")

            # Decide colour based on temperature
            if temp < 20:
                # Blue
                set_rgb_color(0, 0, 255)
            elif temp <= 28:
                # Green
                set_rgb_color(0, 255, 0)
            else:
                # Red
                set_rgb_color(255, 0, 0)

        except Exception as e:
            print("Error:", e)

        time.sleep(1)
