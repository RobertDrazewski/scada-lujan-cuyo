import time
import requests
import numpy as np
from datetime import datetime
import random

class PozoSimulado:
    def __init__(self, id, nombre, lat, lng):
        self.id = id
        self.nombre = nombre
        self.lat = lat
        self.lng = lng
        self.temp_base = 60.0
        self.fallando = False
        self.incremento_falla = 0
        self.bateria = random.randint(70, 100)

    def generar_dato(self):
        ruido = np.random.normal(0, 0.4)
        if self.fallando:
            self.incremento_falla += 0.5
        
        temp_actual = self.temp_base + ruido + self.incremento_falla
        estado = "NORMAL"
        if self.incremento_falla > 4: estado = "ADVERTENCIA"
        if self.incremento_falla > 8: estado = "CRÍTICO"

        return {
            "sensor_id": self.id,
            "nombre": self.nombre,
            "timestamp": datetime.now().strftime("%H:%M:%S"),
            "lectura": round(temp_actual, 2),
            "estado": estado,
            "bateria": self.bateria,
            "lat": self.lat,
            "lng": self.lng
        }

# --- CONFIGURACIÓN DE 10 POZOS EN LUJÁN DE CUYO ---
pozos = [
    PozoSimulado(f"P-{i:03}", f"Pozo Extracción {i}", -33.05 + (i*0.002), -68.89 + (i*0.002))
    for i in range(1, 11)
]

# Forzamos falla en el Pozo 3 y 7 para probar el mapa
pozos[2].fallando = True
pozos[6].fallando = True

URL_SERVIDOR = "http://localhost:3000/api/telemetria"

try:
    print("🚀 Transmitiendo datos de 10 pozos a la red...")
    while True:
        for pozo in pozos:
            dato = pozo.generar_dato()
            try:
                requests.post(URL_SERVIDOR, json=dato, timeout=0.5)
                print(f"📡 {dato['nombre']} | {dato['lectura']}°C | {dato['estado']}")
            except:
                print("❌ Error de conexión")
            time.sleep(0.5) # Enviamos uno cada medio segundo para no saturar
except KeyboardInterrupt:
    print("\nSimulación detenida.")