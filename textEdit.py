import json
from db import MySQL

class EditText():
    
    def JsonToDict(msg):
        jsonData = json.loads(msg)
        print(jsonData)
        return jsonData    
    
    def editData(msg_dict,mydb):
        mac = msg_dict['MAC']
        dateTime = msg_dict['Time']
        msg_newdict = msg_dict.items()
        values = []
        for d in msg_newdict:
            if not ('MAC' in d or 'Time' in d):
                values.append(d)
        DeviceSelect = MySQL.SelectDevice(mydb, mac)
        if (DeviceSelect):
            for value in values:
                val = (mac,dateTime,value[0], value[1])
                print(f"Key:{value[0]}\nValue:{value[1]}")
                if value[1] is not None:
                    MySQL.InsertValue(mydb, val)
                    print("daten wurden in die DB gespeichert!")
                else:
                    print(f"Der Wert:{value[1]} des Key:{value[0]} ist None, das wird nicht in die Datenbank geschrieben.")
        else:
            val = (mac, "device")
            MySQL.InsertDevice(mydb, val)
            print("Device wurde in der DB erfasst!")