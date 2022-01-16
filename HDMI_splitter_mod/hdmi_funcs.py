from machine import Pin
from time import sleep

analog_switch = Pin(16,Pin.OUT, Pin.PULL_DOWN)
led_status1 = Pin(15,Pin.IN,Pin.PULL_UP)
led_status2 = Pin(14,Pin.IN,Pin.PULL_UP)
led_status3 = Pin(13,Pin.IN,Pin.PULL_UP)


def button_sim():
    analog_switch.value(1)
    sleep(0.1)
    analog_switch.value(0)


def get_current():
    if ((led_status1.value() + led_status1.value() + led_status1.value()) > 2):
        if led_status1.value() == 0:
            return 1
        if led_status2.value() == 0:
            return 2
        if led_status3.value() == 0:
            return 3
    else:
        return -1

def toggle_to(des_hdmi):
    curr = get_current()
    start = get_current()
    i = 0
    if curr != -1:
        while (str(curr) != des_hdmi):
            button_sim()
            print(curr)
            sleep(1)
            curr = get_current()
            i += 1
            if i > 2 and curr==start:
                break
