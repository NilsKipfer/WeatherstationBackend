import paho.mqtt.client as mqtt
from db import MySQL
from variables import Variables 
from textEdit import EditText

def on_connect(client, userdata, flags, rc):
	client.subscribe(Variables.mqtt_topic)

def on_message(client, userdata, msg):
    msg_dict = EditText.JsonToDict(msg.payload)
    EditText.editData(msg_dict,mydb)
    
# MQTT Create Client
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

# MQTT Connection
client.connect(Variables.mqtt_broker,Variables.mqtt_port,Variables.mqtt_keepalive)
# DB Connection
mydb = MySQL.connect()

client.loop_forever()