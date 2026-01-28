from gpiozero import RGBLED
import random

class Rgbled:
    def __init__(self, red_pin, green_pin, blue_pin, anode=True):
      
        #Initialize the RGB LED.
        #anode=True for common anode
        self.led = RGBLED(
            red=red_pin,
            green=green_pin,
            blue=blue_pin,
            active_high=not anode)

    def set_color(self, r_val, g_val, b_val):
        #"""Set LED color using values from 0–100"""
        self.led.red = r_val / 100
        self.led.green = g_val / 100
        self.led.blue = b_val / 100

    def random_color(self):
        #"""Set the LED to a random color"""
        r = random.randint(0, 100)
        g = random.randint(0, 100)
        b = random.randint(0, 100)
        self.set_color(r, g, b)
        print(f"Random color: R={r}, G={g}, B={b}")

    def turn_off(self):
        #"""Turn off the LED and release GPIO"""
        self.led.close()




    









      #   key = input("Enter R/G/B to light that color: ")
      #   if key.upper() == 'R':
      #    setColor(100, 0, 0)
      #   elif key.upper() == 'G':
      #       setColor(0, 100, 0)
      #   elif key.upper() == 'B':
      #          setColor(0, 0, 100)









#=====================another code example but slightly different========================================#




# import RPi.GPIO as GPIO
# import time

# colors = [0xFF0000, 0x00FF00, 0x0000FF, 0xFFFF00, 0x00FFFF, 0xFF00FF, 0xFFFFFF, 0x9400D3]
# pins = {'pin_R':11, 'pin_G':12, 'pin_B':13}  # pins is a dict

# GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
# for i in pins:
#         GPIO.setup(pins[i], GPIO.OUT)   # Set pins' mode is output
#         GPIO.output(pins[i], GPIO.HIGH) # Set pins to high(+3.3V) to off led

# p_R = GPIO.PWM(pins['pin_R'], 2000)  # set Frequece to 2KHz
# p_G = GPIO.PWM(pins['pin_G'], 2000)
# p_B = GPIO.PWM(pins['pin_B'], 2000)

# p_R.start(0)      # Initial duty Cycle = 0(leds off)
# p_G.start(0)
# p_B.start(0)

# def map(x, in_min, in_max, out_min, out_max):
#         return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

# def setColor(col):   # For example : col = 0x112233
#         R_val = (col & 0x110000) >> 16
#         G_val = (col & 0x001100) >> 8
#         B_val = (col & 0x000011) >> 0

#         R_val = map(R_val, 0, 255, 0, 100)
#         G_val = map(G_val, 0, 255, 0, 100)
#         B_val = map(B_val, 0, 255, 0, 100)

#         p_R.ChangeDutyCycle(100-R_val)     # Change duty cycle
#         p_G.ChangeDutyCycle(100-G_val)
#         p_B.ChangeDutyCycle(100-B_val)

# try:
#         while True:
#                 for col in colors:
#                         setColor(col)
#                         time.sleep(1.0)
# except KeyboardInterrupt:
#         p_R.stop()
#         p_G.stop()
#         p_B.stop()
#         for i in pins:
#                 GPIO.output(pins[i], GPIO.HIGH)    # Turn off all leds
#         GPIO.cleanup()



#=====================another code example but slightly different========================================#


# from gpiozero import RGBLED
# from time import sleep

# # Define a list of colors for the RGB LED in RGB format (Red, Green, Blue).
# # Each color component ranges from 0 (off) to 1 (full intensity).
# COLORS = [(1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 1, 0), (1, 0, 1), (0, 1, 1)]

# # Initialize an RGB LED. Connect the red component to GPIO 17, green to GPIO 18, and blue to GPIO 27.
# rgb_led = RGBLED(red=17, green=18, blue=27)

# try:
#     # Continuously cycle through the defined colors.
#     while True:
#         for color in COLORS:
#             # Set the RGB LED to the current color.
#             rgb_led.color = color
#             # Output the current color to the console.
#             print(f"Color set to: {color}")
#             # Wait for 1 second before switching to the next color.
#             sleep(1)

# except KeyboardInterrupt:
#     # Handle a KeyboardInterrupt (Ctrl+C) to exit the loop gracefully.
#     # GPIO cleanup will be managed automatically by GPIO Zero on script termination.
#     pass