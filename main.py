import sys
sys.path.insert(0, '/src')

from controller import TrafficController
from webserver import start_ap, create_server, handle_request

start_ap()
server = create_server()
controller = TrafficController()

print("Ampelsteuerung läuft...")

while True:
    handle_request(server, controller)
    controller.run_cycle()