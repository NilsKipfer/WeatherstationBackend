import { getSensorValues, updateDevicename, getDevices } from "../modul/mydb_modul.js";


export const showSensorValues = (req, res) => {
    getSensorValues((err, results) => {
        if (err) {
            res.send(err);
        }
        else {
            res.json(results);
        }
    });
}

export const showDevices = (req, res) => {
    getDevices((err, results) => {
        if (err) {
            res.send(err);
        }
        else {
            res.json(results);
        }
    });
}

export const updateDeviceName = (req, res) => {
    const MAC = req.param.MAC;
    const name = req.param.Name;
    updateDevicename(name, MAC, (err, results) => {
        if (err) {
            res.send(err);
        }
        else {
            res.json(results);
        }
    });
}