from pythonosc import udp_client
import json
import time

#functions
def getMessage():
    with open("message.json", 'r') as file:
        temp = json.load(file)
    return temp

#Variables
client = udp_client.SimpleUDPClient("127.0.0.1", 9000)

#Loop to send a message to vrchat every 5 seconds blah blah blah
while True:
    message = getMessage()
    client.send_message("/chatbox/input", [message, True, False])
    print("Sent message {}".format(message))
    time.sleep(5)
