import mysql.connector as mysql
from variables import Variables 

class MySQL:
    def connect():
        mydb = mysql.connect(
            host=Variables.db_host,
            user=Variables.db_user,
            password=Variables.db_password
        )
        return mydb
    
    def SelectDevice(mydb, MAC):
        mycursor = mydb.cursor()
        sql = f"SELECT * FROM Weatherstation.Devices WHERE MACAddress = '{MAC}';"
        mycursor.execute(sql)
        return mycursor.fetchall()
    
    def InsertValue(mydb,val):
        mycursor = mydb.cursor()
        sql = f"INSERT INTO Weatherstation.DataValues (deviceMAC, valuedate, valuekey, valuedata) VALUES ('{val[0]}', '{val[1]}', '{val[2]}', {val[3]});"
        mycursor.execute(sql)
        mydb.commit()
        
    def InsertDevice(mydb,val):
        mycursor = mydb.cursor()
        sql = "INSERT INTO Weatherstation.Devices (MACAddress, deviceName) VALUES (%s, %s);"
        mycursor.execute(sql, val)
        mydb.commit()
    
    def APIGetData(mydb):
        mycursor = mydb.cursor()
        sql = "SELECT MACAddress ,devicename ,valuedate ,valuekey ,valuedata FROM DataValues INNER JOIN Devices ON DataValues.deviceMAC = Devices.MACAddress ORDER BY valuedate DESC LIMIT 3;"
        mycursor.execute(sql)
        return mycursor.fetchall()