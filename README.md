# Car Logs
This project is a real-time data engineering pipeline that streams car sensor logs (e.g., oil level, engine temperature, battery voltage, speed) to monitor the status and health of a vehicle in real time.

The system is designed to:  
- Collect data from simulated car sensors.

- Stream logs using Kafka/Redpanda for scalable event processing.

- Use Redis as a fast in-memory store for caching latest sensor values.

- Process logs in Python for transformations, anomaly detection, and alerting.

## Tech Stack
- Python – Core processing, producers, consumers, and transformations.
- Kafka / Redpanda – Message streaming backbone for scalable, distributed data pipelines.
- Redis – Low-latency cache for storing and retrieving the latest sensor data.
- Docker – Containerized setup for easy local deployment.
- PostgreSQL / TimescaleDB – Persistent storage of logs for analytics and historical queries.
- Grafana + Prometheus – Dashboarding and visualization of car telemetry in real time.

## Features

✅ Simulated car sensors streaming data in real time.  
✅ Kafka/Redpanda for scalable event streaming.  
✅ Redis for instant lookups of latest sensor state.  
✅ Extendable for anomaly detection (e.g., high engine temp alerts).  
✅ Visualization with Grafana dashboards.


## Getting Started
### Prerequisites
- Python 3.10+
- Docker + Docker Compose
- Redis
- Kafka or Redpanda

### Setup
1. Clone the repo:
```commandline
git clone https://github.com/aust21/car-logs.git
cd car-logs
```
2. Spin up Kafka/Redpanda + Redis via Docker:
```commandline
docker-compose up -d
```
    Check services:  
        TimescaleDB → localhost:5432 (user: admin, pass: admin, db: carlogs)  
        Prometheus → http://localhost:9090  
        Grafana → http://localhost:3000(admin/admin)
3. Run the consumer (processes and stores sensor logs):
```commandline
python consumer.py
```