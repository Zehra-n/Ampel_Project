import socket
import network

SSID = 'AmpelPico'
PASSWORD = 'ampel1234'

HTML = """<!DOCTYPE html>
<html>
<head>
  <title>Ampelsteuerung</title>
  <meta name="viewport" content="width=device-width, initial-scale=1">
</head>
<body>
  <h1>Ampelsteuerung</h1>
  <form action="/pedestrian" method="get">
    <button type="submit">Fussgänger: Grün anfordern</button>
  </form>
  <form action="/car" method="get">
    <button type="submit">Auto: Grün anfordern</button>
  </form>
</body>
</html>
"""

def start_ap():
    ap = network.WLAN(network.AP_IF)
    ap.config(essid=SSID, password=PASSWORD)
    ap.active(True)
    print("AP wird gestartet...")
    timeout = 0
    while not ap.active():
        print("warte...")
        timeout += 1
        if timeout > 10:
            print("AP Timeout!")
            break
    print('AP started:', ap.ifconfig())

def create_server():
    addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
    s = socket.socket()
    s.bind(addr)
    s.listen(1)
    s.setblocking(False)
    return s

def handle_request(server_socket, controller):
    try:
        cl, addr = server_socket.accept()
        request = cl.recv(1024).decode()

        if 'GET /pedestrian' in request:
            controller.request_pedestrian()
        elif 'GET /car' in request:
            controller.request_car()

        cl.send('HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')
        cl.send(HTML)
        cl.close()
    except OSError:
        pass