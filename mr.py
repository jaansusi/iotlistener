import paho.mqtt.client as mqtt
import requests
import logging
import json

#logging
logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)
requests_log = logging.getLogger("requests.packages.urllib3")
requests_log.setLevel(logging.DEBUG)
requests_log.propagate = True

#variables
mqttUrl = "kek.certustec.ee"
mqttUser = "jaansusi"
mqttPass = "password1"
apiUrl = "http://kek.certustec.ee/api/v1/"
apiToken = "6Lf4lMfstamb3Y9L76fv"
topic = "tele/tasmota_6879C1/SENSOR"
data = {
    "id": 1
}


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe(topic)

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    data = json.loads(msg.payload.decode())
    print(msg.topic+" "+msg.payload.decode())
    r = requests.post(url = apiUrl + apiToken + "/telemetry", json = data["ENERGY"])
    print(r.status_code)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.username_pw_set(mqttUser, password=mqttPass)

client.connect(mqttUrl, 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()
