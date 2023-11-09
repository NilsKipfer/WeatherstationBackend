import db from "../config/mysql.js";

export const getSensorValues = (result) => {
  db.query("SELECT MACAddress ,devicename ,valuedate ,valuekey ,valuedata FROM DataValues INNER JOIN Devices ON DataValues.deviceMAC = Devices.MACAddress WHERE valuedate IN (SELECT MAX(valuedate) FROM DataValues GROUP BY deviceMAC) GROUP BY valuekey ,deviceMac ,valueID ,valuedata ,valuedate ORDER BY valuedate DESC, valuekey DESC;",
  (err, results) => {
    if (err) {
      console.log(err);
      result(err, null);
    } else {
      result(null, results);
    }
  });
};

export const getDevices = (result) => {
  db.query("SELECT MACAddress ,devicename FROM Devices;", (err, results) => {
    if (err) {
      console.log(err);
      result(err, null);
    } else {
      result(null, results);
    }
  });
};

export const updateDevicename = (devicename, mac, result) => {
  db.query("UPDATE Devices SET devicename = ? WHERE MACAddress=?;",
    [devicename, mac],
    (err, results) => {
      if (err) {
        console.log(err);
        result(err, null);
      } else {
        result(null, results);
      }
    });
};