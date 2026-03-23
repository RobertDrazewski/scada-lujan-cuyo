# 🛰️ SCADA Luján de Cuyo: Real-Time Industrial Telemetry Platform

A high-performance **SCADA (Supervisory Control and Data Acquisition)** solution designed for real-time monitoring of oil/water extraction wells. This project integrates a robust Node.js telemetry engine with a React-based mission control dashboard.

---

## 🚀 Technical Stack

### **Frontend (Mission Control)**
* **React.js**: Functional components and Hooks for state management.
* **Leaflet.js**: Interactive geospatial mapping with dynamic SVG/CSS markers.
* **Lucide React**: Industrial-grade iconography.
* **React Router**: Multi-view navigation (Dashboard, Inventory, and Analytics).
* **ECharts**: High-performance time-series data visualization.

### **Backend (Telemetry Engine)**
* **Node.js & Express**: RESTful API architecture.
* **Simulation Logic**: Algorithmic generation of thermal and power telemetry.

---

## 🛠️ Key Functionalities

* **Geospatial Intelligence**: Real-time map with dynamic color-coding (Green/Yellow/Red) based on well health.
* **Intelligent KPI Cards**: Quick-glance metrics (Critical, Observation, Normal) with integrated modal filtering for rapid response.
* **High-Stability Popups**: Custom-engineered UI popups with anti-flicker logic for seamless operator interaction.
* **Deep-Dive Analytics**: Individual well tracking with historical data trends.
* **Full Inventory View**: Comprehensive list of all field assets with real-time status updates.

---

## 🔮 Future Vision & Roadmap

This project is designed as a **highly scalable and monetizable MVP (Minimum Viable Product)**. The architecture is ready to transition from simulation to industrial production:

1.  **Industrial Connectivity (LoRaWAN)**: Replace the simulation engine with real-world **LoRa** gateway integration. This will allow long-range, low-power data transmission from remote oil fields where cellular coverage is non-existent.
2.  **Database Persistence**: Implementation of a Time-Series Database (InfluxDB or PostgreSQL with TimescaleDB) to store years of historical telemetry.
3.  **Predictive AI**: Implementation of Machine Learning models to predict well failure before it occurs (Predictive Maintenance).
4.  **Security & Multi-tenancy**: Robust Auth0/JWT integration for secure, multi-user industrial environments.

> **Business Perspective**: This is a fully feasible project aimed at the digital transformation of the energy sector. By reducing field visit frequency through remote LoRa monitoring, companies can achieve significant operational cost reductions (OPEX).

---

## ⚙️ Installation

1. **Clone the repository**:
   ```bash
   git clone [https://github.com/RobertDrazewski/scada-lujan-cuyo.git](https://github.com/RobertDrazewski/scada-lujan-cuyo.git)

2. Install dependencies: npm install
3. Start the environment: npm start
   