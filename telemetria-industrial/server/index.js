const express = require('express');
const cors = require('cors');
const bodyParser = require('body-parser');

const app = express();
const PORT = 3000;

// Middlewares
app.use(cors());
app.use(bodyParser.json());

// Base de datos temporal en memoria (luego usaremos una real)
let lecturasRecibidas = [];

// RUTA 1: Recibir datos del simulador (POST)
app.post('/api/telemetria', (req, res) => {
    const dato = req.body;
    
    // Agregamos el dato al inicio del array
    lecturasRecibidas.unshift(dato);
    
    // Mantener solo las últimas 20 lecturas
    if (lecturasRecibidas.length > 20) lecturasRecibidas.pop();

    console.log(`[LECTURA RECIBIDA] Sensor: ${dato.sensor_id} | Temp: ${dato.lectura}°C | Status: ${dato.estado}`);
    
    res.status(201).json({ message: "Dato recibido correctamente" });
});

// RUTA 2: Entregar datos al Dashboard (GET)
app.get('/api/telemetria', (req, res) => {
    res.json(lecturasRecibidas);
});

app.listen(PORT, () => {
    console.log(`==========================================`);
    console.log(`🚀 SERVIDOR DE TELEMETRÍA CORRIENDO`);
    console.log(`📍 URL: http://localhost:${PORT}`);
    console.log(`==========================================`);
});