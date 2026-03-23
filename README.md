# 🛰️ Sistema SCADA de Telemetría en Tiempo Real

Este proyecto es una plataforma **SCADA (Supervisory Control and Data Acquisition)** diseñada para el monitoreo de 10 pozos de extracción en tiempo real. Integra un simulador de sensores basado en Node.js y un Dashboard interactivo en React.

## 🚀 Arquitectura del Sistema

### 1. Backend (Simulador de Telemetría)
- **Tecnología:** Node.js / Express.
- **Funcionalidad:** Genera datos aleatorios pero lógicos de **Temperatura** y **Batería** para 10 sensores fijos con coordenadas geográficas reales.
- **Lógica de Estados:** - `NORMAL`: Lecturas estables.
  - `OBSERVACIÓN`: Variaciones moderadas.
  - `CRÍTICO`: Alertas por alta temperatura o batería baja.
- **Actualización:** Envía datos cada 1 segundo vía API REST.

### 2. Frontend (Dashboard Operativo)
- **Tecnología:** React.js + React Router + Leaflet.
- **Componentes Clave:**
  - **Mapa Dinámico:** Visualización geográfica con iconos circulares que cambian de color (Rojo/Amarillo/Verde) según el estado del sensor.
  - **KPI Cards:** Indicadores superiores interactivos que cuentan pozos por estado. Al hacer clic, abren un modal con el listado filtrado.
  - **Popups Anti-Parpadeo:** Ventanas de información compactas y estables para lecturas rápidas sobre el mapa.
  - **Historial Detallado:** Integración con ECharts para visualizar gráficamente el comportamiento histórico de cada pozo.

## 🛠️ Instalación y Uso

1. **Clonar el repositorio:**
   ```bash
   git clone [https://github.com/RobertDrazewski/scada-lujan-cuyo.git]