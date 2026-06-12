from traffic_light import TrafficLight
from utime import ticks_ms

GREEN_DURATION = 5000
TRANSITION_DELAY = 1000

class TrafficController:
    def __init__(self):
        self.car_light = TrafficLight(6, 7, 8)
        self.pedestrian_light = TrafficLight(18, 19, 20)

        self.pedestrian_requested = False
        self.car_requested = False

        self.state = 'car_green'
        self.state_start = ticks_ms()

        self.car_light.set_green()
        self.pedestrian_light.set_red()

    def request_pedestrian(self):
        self.pedestrian_requested = True

    def request_car(self):
        self.car_requested = True

    def run_cycle(self):
        now = ticks_ms()
        elapsed = now - self.state_start

        if self.state == 'car_green':
            if self.pedestrian_requested and elapsed > GREEN_DURATION:
                self.car_light.set_yellow()
                self._set_state('car_yellow')

        elif self.state == 'car_yellow':
            if elapsed > TRANSITION_DELAY:
                self.car_light.set_red()
                self._set_state('car_red')

        elif self.state == 'car_red':
            if elapsed > TRANSITION_DELAY:
                self.pedestrian_light.set_red_yellow()
                self._set_state('pedestrian_red_yellow')

        elif self.state == 'pedestrian_red_yellow':
            if elapsed > TRANSITION_DELAY:
                self.pedestrian_light.set_green()
                self._set_state('pedestrian_green')

        elif self.state == 'pedestrian_green':
            if elapsed > GREEN_DURATION:
                self.pedestrian_light.set_yellow()
                self._set_state('pedestrian_yellow')

        elif self.state == 'pedestrian_yellow':
            if elapsed > TRANSITION_DELAY:
                self.pedestrian_light.set_red()
                self._set_state('pedestrian_red')

        elif self.state == 'pedestrian_red':
            if elapsed > TRANSITION_DELAY:
                self.pedestrian_requested = False
                self.car_light.set_red_yellow()
                self._set_state('car_red_yellow')

        elif self.state == 'car_red_yellow':
            if elapsed > TRANSITION_DELAY:
                self.car_light.set_green()
                self._set_state('car_green')

    def _set_state(self, new_state):
        self.state = new_state
        self.state_start = ticks_ms()