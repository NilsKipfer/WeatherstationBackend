import express from 'express'
import { showDevices, showSensorValues, updateDeviceName } from '../controller/mydb_controller.js';

const router = express.Router();

router.get("/api/sensorValues", showSensorValues);

router.get("/api/device", showDevices);

router.put('/api/device/:MAC', updateDeviceName);

export default router;