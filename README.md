# Real-time Change Data Capture Pipeline

## Overview

This project implements a robust, real-time Change Data Capture (CDC) pipeline designed to ingest, process, and store live flight data. It leverages a modern data stack to ensure data consistency, scalability, and real-time analytics capabilities.

The core objective is to capture changes from a transactional database (PostgreSQL) and stream them efficiently to an analytical data warehouse (Snowflake) for real-time reporting and analysis. The entire process is automated using GitHub Actions, which also handles critical data consistency checks.

## System Architecture

The following diagram illustrates the flow of data and the interaction between different components:

![Architecture Diagram](architecture-diagram.png) <!-- Replace with actual path -->

### Key Components

- **Real-time Flights Data Simulator (API):** Acts as the data producer, generating live flight data and pushing it into PostgreSQL.
- **PostgreSQL:** The primary transactional database where raw flight data is initially stored and updated.
- **Debezium:** An open-source distributed platform for change data capture. It monitors PostgreSQL for row-level changes (inserts, updates, deletes) and streams these events.
- **Apache Kafka:** A distributed streaming platform used to reliably transport the change events captured by Debezium.
- **Snowflake Streaming:** Utilized to efficiently ingest data streams from Kafka directly into Snowflake tables.
- **Snowflake:** The cloud data warehouse where the processed and transformed flight data is stored, optimized for analytical queries.
- **GitHub Actions:** Automates the entire deployment process, including infrastructure provisioning (if applicable), application deployment, and execution of critical data consistency checks between PostgreSQL and Snowflake.
- **Monitoring (Optional):**
  - **Datadog:** Can be integrated for real-time monitoring and logging.
  - **Power BI:** Can be used for dashboards and business intelligence.

> **Note:** Datadog and Power BI are supported but not configured in this repo.

## Features

- ✅ Real-time Data Ingestion
- 🔄 Change Data Capture (CDC)
- ⚡ Scalable Event Streaming with Kafka
- 🤖 Automated Deployment & Validation via GitHub Actions
- 📊 Optional Monitoring via Datadog & Power BI
- 🔐 Data Consistency Checks Between PostgreSQL and Snowflake

## Prerequisites

Make sure you have the following installed:

- Docker & Docker Compose
- Access to a Snowflake account
- GitHub account
- Python (for simulator scripts, optional)
- Datadog (optional)
- Power BI Desktop (optional)

## Installation

### 1. Clone the Repository

```bash
git clone <your-repository-url>
cd <your-repository-name>
