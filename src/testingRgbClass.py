from gpioRgb import Rgbled
import time
#importing the class

if __name__ == '__main__':
    print('Program is starting ...')
    led = Rgbled(17, 18, 27, anode=True)
    # led = Rgbled(15, 20, 23, anode=True) #<-- this is how you would change the pin numbers if you wanted to use alternitive pins
    #here i set the GPIO pins on the pi

    try:
        while True:
            led.random_color()
            time.sleep(0.6)
            #called the random function and set the ammount for delay between colors 

    except KeyboardInterrupt:
        print("Stopping program")
        led.turn_off()
            #gave the user to end the loop
            #ended the loop
