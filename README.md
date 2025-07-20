Real-time Change Data Capture Pipeline
This project implements a robust, real-time Change Data Capture (CDC) pipeline designed to ingest, process, and store live flight data. It leverages a modern data stack to ensure data consistency, scalability, and real-time analytics capabilities.
🚀 Project Overview
The core objective of this pipeline is to capture changes from a transactional database (PostgreSQL) and stream them efficiently to an analytical data warehouse (Snowflake) for real-time reporting and analysis. The entire process is automated using GitHub Actions, which also handles critical data consistency checks.
✨ Architecture
The pipeline is built around several key components working in concert:
Real-time Flights Data Simulator (API): Acts as the data producer, generating live flight data and pushing it into PostgreSQL.
PostgreSQL: The primary transactional database where raw flight data is initially stored and updated.
Debezium: An open-source distributed platform for change data capture. It monitors PostgreSQL for row-level changes (inserts, updates, deletes) and streams these events.
Apache Kafka: A distributed streaming platform used to reliably transport the change events captured by Debezium. It acts as a central nervous system for the data flow.
Snowflake Streaming: Utilized to efficiently ingest data streams from Kafka directly into Snowflake tables.
Snowflake: The cloud data warehouse where the processed and transformed flight data is stored, optimized for analytical queries.
GitHub Actions: Automates the entire deployment process, including infrastructure provisioning (if applicable), application deployment, and execution of critical data consistency checks between PostgreSQL and Snowflake.
Monitoring (Datadog & Power BI - Potential Setup):
Datadog: Can be integrated for real-time monitoring and logging of the pipeline's health and performance.
Power BI: Can be used to provide dashboards and visualizations for data consistency validation and business intelligence.
Note: While the architecture supports these monitoring tools, their specific setup is not included in this repository but can be implemented.
Architecture Diagram
The following diagram illustrates the flow of data and the interaction between different components:
🎯 Key Features
Real-time Data Ingestion: Captures and processes live flight data as it occurs.
Change Data Capture (CDC): Efficiently identifies and streams only the changed data, reducing load and improving performance.
Scalable Event Streaming: Leverages Kafka for high-throughput, fault-tolerant data streaming.
Automated Deployment & Validation: GitHub Actions ensures continuous integration and deployment, along with automated data consistency checks.
Comprehensive Monitoring (Optional): The architecture is designed to integrate with tools like Datadog for operational monitoring and Power BI for business-level data validation.
Data Consistency: Regular checks are performed to ensure data integrity between source (PostgreSQL) and destination (Snowflake).
🛠️ Setup and Installation
To set up and run this pipeline, you will need to configure each component individually. Below is a high-level guide. Please refer to the official documentation for each tool for detailed installation and configuration instructions.
Prerequisites
Docker (recommended for local development of Kafka, Debezium, PostgreSQL)
Access to a Snowflake account
GitHub account for GitHub Actions
Datadog account (optional, for monitoring)
Power BI Desktop (optional, for dashboards)
Steps
Flight Data Simulator:
Set up your real-time flight data simulator to start pushing data to PostgreSQL.
(Further instructions depend on the simulator's implementation.)
PostgreSQL:
Install and configure a PostgreSQL instance.
Create the necessary database and tables for flight data.
Ensure logical decoding is enabled for Debezium.
Debezium:
Deploy Debezium (e.g., as a Kafka Connect connector).
Configure a PostgreSQL connector to capture changes from your flight data tables.
Apache Kafka:
Set up a Kafka cluster (e.g., using Docker Compose for local testing, or a managed service).
Ensure Kafka topics are created for Debezium to publish to.
Snowflake:
Create a Snowflake account and a dedicated database/schema for this project.
Configure Snowflake Streaming to ingest data from the Kafka topics.
Define the target tables in Snowflake to match the incoming data schema.
GitHub Actions:
Configure your GitHub repository with workflows for:
Automated deployment of pipeline components.
Scheduled or event-triggered data consistency checks (e.g., SQL queries comparing row counts or checksums between PostgreSQL and Snowflake).
Snowflake Workflow Automation: A dedicated GitHub workflow is implemented to connect to your Snowflake instance and execute SQL scripts. This workflow is specifically configured to trigger automatically whenever changes are pushed to the snowflake.sql file within the repository, ensuring that your Snowflake schema and data transformations are always up-to-date with your code.
Monitoring (Datadog & Power BI - Optional Setup):
Datadog: Integrate Datadog agents with your servers/containers running Kafka, Debezium, and PostgreSQL. Configure custom metrics and dashboards.
Power BI: Connect Power BI to your Snowflake instance to build dashboards for data validation and operational insights.
🚀 Usage
Once all components are set up and running:
Start Data Ingestion: Initiate the real-time flight data simulator to begin populating PostgreSQL.
Monitor Pipeline Flow: Observe the data flowing through Debezium to Kafka, and then into Snowflake.
Check Consistency: Monitor the GitHub Actions workflows for the results of data consistency checks.
Analyze Data: Use Snowflake for ad-hoc queries or Power BI dashboards for visual analysis of the flight data.
🤝 Contributing
Contributions are welcome! If you have suggestions for improvements, bug fixes, or new features, please open an issue or submit a pull request.
📄 License
This project is open-source and available under the MIT License.
