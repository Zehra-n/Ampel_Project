from traffic_light import TrafficLight
from utime import sleep

GREEN_DURATION = 5
MIN_CAR_GREEN_DURATION = 3

class TrafficController:
    def __init__(self):
        # Ampel 1 = Autos: R=GPIO6, Y=GPIO7, G=GPIO8
        # Ampel 2 = Fussgänger: R=GPIO18, Y=GPIO19, G=GPIO20
        self.car_light = TrafficLight(6, 7, 8)
        self.pedestrian_light = TrafficLight(18, 19, 20)

        self.pedestrian_requested = False
        self.car_requested = False

        self.car_light.set_green()
        self.pedestrian_light.set_red()

    def request_pedestrian(self):
        self.pedestrian_requested = True

    def request_car(self):
        self.car_requested = True

    def run_cycle(self):
        if self.pedestrian_requested:
            self._give_pedestrian_green()
        elif self.car_requested:
            self._give_car_green()
        else:
            sleep(1)

    def _give_pedestrian_green(self):
        self.car_light.transition_to_red()
        self.pedestrian_light.transition_to_green()
        sleep(GREEN_DURATION)
        self.pedestrian_light.transition_to_red()
        self.car_light.transition_to_green()
        self.pedestrian_requested = False

    def _give_car_green(self):
        self.pedestrian_light.transition_to_red()
        self.car_light.transition_to_green()
        sleep(MIN_CAR_GREEN_DURATION)
        self.car_requested = False