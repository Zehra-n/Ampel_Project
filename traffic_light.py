from machine import Pin

class TrafficLight:
    def __init__(self, pin_red, pin_yellow, pin_green):
        self.red = Pin(pin_red, Pin.OUT)
        self.yellow = Pin(pin_yellow, Pin.OUT)
        self.green = Pin(pin_green, Pin.OUT)
        self.all_off()

    def all_off(self):
        self.red.off()
        self.yellow.off()
        self.green.off()

    def set_red(self):
        self.all_off()
        self.red.on()

    def set_red_yellow(self):
        self.all_off()
        self.red.on()
        self.yellow.on()

    def set_green(self):
        self.all_off()
        self.green.on()

    def set_yellow(self):
        self.all_off()
        self.yellow.on()

def transition_to_green(self):
    self.set_red_yellow()
    self.set_green()

def transition_to_red(self):
    self.set_yellow()
    self.set_red()