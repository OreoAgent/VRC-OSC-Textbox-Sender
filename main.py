from pythonosc import dispatcher
from pythonosc import osc_server
from pythonosc import udp_client
import json
import time

#functions
def getMessage():
    with open("message.json", 'r') as file:
        temp = json.load(file)
    return temp

#Variables
dispatcher = dispatcher.Dispatcher()
server = osc_server.ThreadingOSCUDPServer(("127.0.0.1", 9001), dispatcher)
client = udp_client.SimpleUDPClient("127.0.0.1", 9000)
print(f"Serving on {server.server_address}")

#Loop to send a message to vrchat every 5 seconds blah blah blah
while True:
    message = getMessage()
    client.send_message("/chatbox/input", [message, True, False])
    print("Sent message {}".format(message))
    time.sleep(5)