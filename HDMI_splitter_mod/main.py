from machine import Pin
from time import sleep
import hdmi_funcs

# Pins for the HDMI switch
analog_switch = Pin(16,Pin.OUT, Pin.PULL_DOWN)
led_status1 = Pin(15,Pin.IN,Pin.PULL_UP)
led_status2 = Pin(14,Pin.IN,Pin.PULL_UP)
led_status3 = Pin(13,Pin.IN,Pin.PULL_UP)

# Pins for the relay board
relayCtrl1 = Pin(21,Pin.OUT,Pin.PULL_DOWN) # Relay IN
# relayCtrl2 = Pin(20,Pin.OUT,Pin.PULL_DOWN)
# relayCtrl3 = Pin(19,Pin.OUT,Pin.PULL_DOWN)
# relayCtrl4 = Pin(18,Pin.OUT,Pin.PULL_DOWN)

#relayCtrl1 = Pin(21,Pin.OUT,Pin.PULL_DOWN)
#relayCtrl1 = Pin(21,Pin.OUT,Pin.PULL_DOWN)

while 1:
    
    inp = input("Go to HDMI ")
    hdmi_funcs.toggle_to(inp)
#     print(hdmi_funcs.get_current())
    
    sleep(0.5)




