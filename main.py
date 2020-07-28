import paho.mqtt.client as mqtt
import logging
import json

import config as cfg
import database as db

#logging
if (cfg.debug):
    logging.basicConfig()
    logging.getLogger().setLevel(logging.DEBUG)
    requests_log = logging.getLogger("requests.packages.urllib3")
    requests_log.setLevel(logging.DEBUG)
    requests_log.propagate = True

deviceQuery = db.query("SELECT topic, id FROM devices;", returnData = True)
if (cfg.debug):
    print("Devices returned by database:", deviceQuery)

devices = dict()
for topic, id in deviceQuery:
    devices.setdefault(topic, id)

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    topics = list(map(lambda a : (a, 0), devices))
    if (cfg.debug):
        print("Subscribing to topics:", topics)
    client.subscribe(topics)

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    data = json.loads(msg.payload.decode())
    if (cfg.debug):
        print("Retrieved message from topic", msg.topic, ":", data)
    sqlData = data["ENERGY"]
    sqlData["Time"] = data["Time"]
    sqlData["DeviceId"] = devices[msg.topic]
    addTelemetry = ("INSERT INTO telemetry_powr2 "
                "(device_id, time, today, period, power, voltage, current, factor, apparent_power, reactive_power, yesterday, total, total_start_time)"
                "VALUES (%(DeviceId)s, %(Time)s, %(Today)s, %(Period)s, %(Power)s, %(Voltage)s, %(Current)s, %(Factor)s, %(ApparentPower)s, %(ReactivePower)s, %(Yesterday)s, %(Total)s, %(TotalStartTime)s);")
    db.query(addTelemetry, sqlData, False)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.username_pw_set(cfg.mqtt["username"], password=cfg.mqtt["password"])

client.connect(cfg.mqtt["host"], 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()


