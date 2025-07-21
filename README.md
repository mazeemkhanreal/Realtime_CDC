# 🛰️ Real-time Change Data Capture (CDC) Pipeline

![Architecture](./CDC.svg)

## Overview

This project demonstrates a **real-time Change Data Capture (CDC) pipeline** for ingesting and analyzing live flight data. It is designed to reflect a modern, production-grade data engineering stack that can handle high-velocity streaming data, preserve transactional consistency, and power downstream analytics in near real time.

The goal is to replicate changes happening in a **PostgreSQL** database — populated from a live **external API** — and stream those changes all the way into **Snowflake**, where analytical dashboards or BI tools can consume them.

---

## Why This Project?

In today’s data-driven environments, **batch pipelines** are often not fast enough. Businesses need:
- **Real-time insight** into operations
- **Immediate responses** to data changes
- **Decoupled microservices** powered by streams

This project simulates such a system — starting from an external data source and ending at an analytical warehouse, with a fully automated and scalable pipeline in between.

---

## Architecture

The CDC pipeline consists of several key components:

### 🔄 1. Data Source – Flight API
A live aviation API (e.g., OpenSky) continuously provides real-time flight data such as aircraft positions and statuses. This data simulates the operational system of a business (e.g., a booking system).

### 🗄️ 2. PostgreSQL
The API ingests data into a transactional PostgreSQL database. It behaves like a source-of-truth OLTP system where inserts/updates/deletes occur frequently.

### 🔁 3. Debezium + Kafka
Debezium monitors the PostgreSQL write-ahead log (WAL) and captures row-level changes in real time. These changes are streamed into Kafka topics for further processing.

### 🔌 4. Kafka Connect + Snowflake Sink Connector
Kafka Connect reads change records from Kafka topics and streams them into Snowflake using the official Snowflake Sink Connector. The data lands in analytical tables, ready for querying.

### 🧊 5. Snowflake
Snowflake acts as the real-time analytical engine. As changes propagate from the source, Snowflake remains consistently up to date with the latest state of the operational data.

### ⚙️ 6. GitHub Actions
All relevant scripts (e.g., Snowflake DDLs, connectors) are managed via GitHub Actions to automate deployment and integration workflows.

---

## Key Technologies

| Component           | Technology                        |
|---------------------|-----------------------------------|
| Data Source         | OpenSky API (live flight data)    |
| Database            | PostgreSQL                        |
| Change Data Capture | Debezium                          |
| Messaging System    | Apache Kafka                      |
| Stream Integration  | Kafka Connect + Snowflake Sink    |
| Data Warehouse      | Snowflake                         |
| Containerization    | Docker Compose                    |
| CI/CD               | GitHub Actions                    |

---

## How Data Flows

1. External API pushes real-time flight data → PostgreSQL
2. Debezium detects changes in PostgreSQL (insert/update/delete)
3. Kafka receives CDC events from Debezium topics
4. Kafka Connect streams data into Snowflake via Snowflake Sink Connector
5. GitHub Actions ensures automated deployment of schema and connectors
6. Analysts can query real-time data in Snowflake for insights

---

## Real-World Applications

- **Aviation Dashboards**: Real-time updates of flights, delays, or re-routes.
- **E-commerce**: Track inventory, orders, or customer activity in real time.
- **Banking**: Transaction auditing and fraud detection pipelines.
- **Logistics**: Monitor shipments, fleet movement, and ETA predictions.

---

## Diagram (CDC.svg)

The diagram illustrates the full data pipeline, showing the movement of data and the roles of each component.

> 🖼️ *If viewing on GitHub, scroll up to see the visual architecture diagram above.*

---

## Future Improvements

- Add schema versioning and validation with Avro + Schema Registry  
- Implement data quality checks before writing to Snowflake  
- Build a lightweight dashboard using Streamlit or Superset  
- Add monitoring/alerting via Prometheus + Grafana

---

## Author

**Muhammad Azeem Khan**  
Data Engineer | Automation Analyst  
[Your LinkedIn] | [https://mazeemkhanreal.github.io/resume/] | [mazeemkhanq@gmail.com]
