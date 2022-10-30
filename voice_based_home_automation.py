import wiotp.sdk.device
import time
import os
import datetime
import random
myConfig = {
	"identity":{
	    "orgId": "fbeobe",
	    "typeId": "NodeMCU",
            "deviceId":"12345"
	},
        "auth": {
            "token":"12345678"
	}
}  
def myCommandCallback(cmd):
    print("Message received from IBM IoT Platform: %s " % cmd.data['command'])
    m=cmd.data['command']
    if(m=="light on"):
       print("Light is switched ON")
    elif(m=="light off"):
       print("Light is switched OFF")
    if(m=="fan on"):
       print("Fan is switched ON")
    elif(m=="fan off"):
       print("Fan is switched OFF")
client = wiotp.sdk.device.DeviceClient(config=myConfig, logHandlers=None)
client.connect()

while True:
	client.commandCallback = myCommandCallback
	time.sleep(10)
	print("Light is switched ON")
	time.sleep(20000)
client.disconnect()
