# 🏗️ Enterprise Real-Time Data Pipeline

A production-ready real-time data pipeline leveraging Kafka, Avro, Spark Structured Streaming, and Snowflake. Built for reliability, scalability, and performance in modern data engineering environments.

---

## 📦 Features

- Kafka + Avro producer for streaming real-time events
- Schema Registry integration for Avro schema enforcement
- Dockerized stack with Zookeeper, Kafka, Schema Registry, Kafka UI
- Spark Structured Streaming consumer (placeholder for extension)
- Snowflake integration with SQL schema templates
- Modular folder structure with configs and Jupyter notebook

---

## 🚀 Usage Guide

### 1. Prerequisites

- Python 3.8+
- Docker & Docker Compose
- Git

Install dependencies:

```bash
pip install -r requirements.txt
```

---

### 2. Start Kafka + Schema Registry Stack

```bash
cd docker
docker-compose up -d
```

- Kafka Broker: `localhost:9092`
- Schema Registry: `http://localhost:8081`
- Kafka UI: [http://localhost:8080](http://localhost:8080)

---

### 3. Run Kafka Producer

```bash
cd kafka
python producer.py
```

Produces stock market data into Kafka using Avro serialization.

---

### 4. (Optional) Spark Streaming Consumer

```bash
cd spark
spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.4.1 stream_to_snowflake.py
```

> 🚧 Add your own logic to `stream_to_snowflake.py` to connect Kafka → Spark → Snowflake.

---

### 5. Snowflake Setup

Use `snowflake/schema.sql` to create target tables. Set your credentials in `config.yaml` or `.env` file.

---

### 6. Jupyter Notebook (Demo / Analytics)

```bash
jupyter notebook notebooks/analytics_demo.ipynb
```

---

## 📁 Folder Structure

```
enterprise-realtime-data-pipeline/
│
├── docker/                # Docker services: Kafka, Zookeeper, Schema Registry
├── kafka/                 # Kafka Avro producer script
├── spark/                 # Spark streaming job (extendable)
├── snowflake/             # Snowflake schema SQL
├── configs/               # config.yaml for credentials and app configs
├── notebooks/             # Jupyter Notebooks for testing/analytics
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ✅ TODOs & Extensions

- Add DLQ (Dead Letter Queue) Kafka topics for failed messages
- Integrate with Airflow for orchestration
- Add Snowflake CDC or micro-batching
- Add CI/CD via GitHub Actions

---

## 👨‍💻 Author

**Yashwanth Pinnapureddy**  
AWS Data Engineer | 8 YOE | Kafka | Spark | Snowflake | Databricks | Python

---

