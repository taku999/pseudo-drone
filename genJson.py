from datetime import datetime
import time,datetime
import json
import random

file_path = "./test.json"

long_base = 35.37283647626263
lat_base = 139.5583354122437
#long_add  =  0.000000000001
#lat_add  =   0.00000000001
long_add  =  0.00001
lat_add  =   0.0001

#long_add  =  0 #for debug
#lat_add  =   0 # for debug
i = 0 

while(True):
    temp = {
        'Time': str(datetime.datetime.now()),
        "g1":{
            'SW': random.randint(0,1),
            'Long': str(long_base + (long_add*i)), 
            'Lat' : str(lat_base + (lat_add*i)),
            'RSSI': str('{:.2f}'.format(random.uniform(-20, -60))),
            'Volt': str('{:.2f}'.format(random.uniform(1, 5))),
            'Temperature': str('{:.2f}'.format(random.uniform(0, 40))),
            'Humidity': str('{:.2f}'.format(random.uniform(0, 40)))
        },
        "c1m":{
            'SW': random.randint(0,1),
            'RSSI': str('{:.2f}'.format(random.uniform(-20, -60))),
            'Volt': str('{:.2f}'.format(random.uniform(1, 5))),
            'Temperature': str('{:.2f}'.format(random.uniform(0, 40))),
            'Humidity': str('{:.2f}'.format(random.uniform(0, 40)))
        },
        "c1s":{
            'SW': random.randint(0,1),
            'RSSI': str('{:.2f}'.format(random.uniform(-20, -60))),
            'Volt': str('{:.2f}'.format(random.uniform(1, 5))),
            'Temperature': str('{:.2f}'.format(random.uniform(0, 40))),
            'Humidity': str('{:.2f}'.format(random.uniform(0, 40)))
        },
        "p1m":{
            'SW': random.randint(0,1),
            'RSSI': str('{:.2f}'.format(random.uniform(-20, -60))),
            'Volt': str('{:.2f}'.format(random.uniform(1, 5))),
            'Temperature': str('{:.2f}'.format(random.uniform(0, 40))),
            'Humidity': str('{:.2f}'.format(random.uniform(0, 40)))
        },
        "p1s":{
            'SW': random.randint(0,1),
            'RSSI': str('{:.2f}'.format(random.uniform(-20, -60))),
            'Volt': str('{:.2f}'.format(random.uniform(1, 5))),
            'Temperature': str('{:.2f}'.format(random.uniform(0, 40))),
            'Humidity': str('{:.2f}'.format(random.uniform(0, 40)))
        }
    }
    with open(file_path, 'w') as f:
        json.dump(temp, f, ensure_ascii=False)
    print(temp)
    i = i + 1
    time.sleep(5)