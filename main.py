import paho.mqtt.client as mqtt
import json
import logging
import os
from datetime import datetime

import yaml

cfg = yaml.safe_load(open("config.yml"))

if cfg["db"]["engine"] == "mysql":
    import db_mysql as db
elif cfg["db"]["engine"] == "sqlite":
    import db_sqlite as db
else:
    raise Exception("DB engine not supported")

if not os.path.exists('logs'):
    os.makedirs('logs')

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('MainLogger')

fh = logging.FileHandler('logs/{:%Y-%m-%d}.log'.format(datetime.now()))
formatter = logging.Formatter('%(asctime)s | %(levelname)-8s | %(lineno)04d | %(message)s')
fh.setFormatter(formatter)

logger.addHandler(fh)
logger.info("Starting script..")

if cfg["debug"]:
    print("Devices in config:", cfg["devices"])

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    topics = list(map(lambda a : (a["device"]["topic"], 0), cfg["devices"]))
    if cfg["debug"]:
        print("Subscribing to topics:", topics)
    client.subscribe(topics)
    logger.info("Script running, listening to {} topic(s)".format(len(topics)))

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    data = json.loads(msg.payload.decode())
    logger.info("Incoming message: " + msg.topic + " - " + str(data))
    if cfg["debug"]:
        print("Retrieved message from topic", msg.topic, ":", data)
    sqlData = data["ENERGY"]
    sqlData["Time"] = data["Time"]
    sqlData["Topic"] = msg.topic
    
    db.insertTelemetry(sqlData)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.username_pw_set(cfg["mqtt"]["username"], password=cfg["mqtt"]["password"])

client.connect(cfg["mqtt"]["host"], 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()


