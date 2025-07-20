Real-time Change Data Capture Pipeline
Overview
This project implements a robust, real-time Change Data Capture (CDC) pipeline designed to ingest, process, and store live flight data. It leverages a modern data stack to ensure data consistency, scalability, and real-time analytics capabilities. The core objective is to capture changes from a transactional database (PostgreSQL) and stream them efficiently to an analytical data warehouse (Snowflake) for real-time reporting and analysis. The entire process is automated using GitHub Actions, which also handles critical data consistency checks.
System Architecture
The following diagram illustrates the flow of data and the interaction between different components:
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
Features
Real-time Data Ingestion: Captures and processes live flight data as it occurs.
Change Data Capture (CDC): Efficiently identifies and streams only the changed data, reducing load and improving performance.
Scalable Event Streaming: Leverages Kafka for high-throughput, fault-tolerant data streaming.
Automated Deployment & Validation: GitHub Actions ensures continuous integration and deployment, along with automated data consistency checks.
Comprehensive Monitoring (Optional): The architecture is designed to integrate with tools like Datadog for operational monitoring and Power BI for business-level data validation.
Data Consistency: Regular checks are performed to ensure data integrity between source (PostgreSQL) and destination (Snowflake).
Prerequisites
Before setting up and running this pipeline, ensure you have the following installed:
Docker and Docker Compose: Recommended for local development and orchestrating Kafka, Debezium, and PostgreSQL.
Access to a Snowflake account: Required for the data warehouse.
GitHub account: Necessary for utilizing GitHub Actions for automation.
Basic understanding of Docker, Kafka, and PostgreSQL.
Datadog account (optional): For comprehensive monitoring.
Power BI Desktop (optional): For data visualization and dashboards.
Installation
Clone the Repository:
If this project is part of a GitHub repository, clone it to your local machine:
git clone <your-repository-url>
cd <your-repository-name>


Install Required Python Libraries (if applicable):
If there are any Python scripts (e.g., for data simulation or local testing utilities) that require specific libraries, install them:
pip install psycopg2-binary faker # Example for a data generator script


Services in the Compose File
This project leverages Docker Compose to orchestrate the core data pipeline services. A docker-compose.yml file (which you would need to create or will find in the repository) defines the following services:
Zookeeper: A centralized service for maintaining configuration information, naming, providing distributed synchronization, and providing group services for Kafka.
Kafka Broker: The distributed streaming platform used for handling real-time data feeds.
Debezium Connect: The Debezium Kafka Connect service configured to capture changes from PostgreSQL.
PostgreSQL: The relational database serving as the source for CDC.
Confluent Control Center (Optional): A web-based tool for managing and monitoring Apache Kafka (if included in your docker-compose.yml).
Debezium UI (Optional): A user interface for managing and monitoring Debezium connectors (if included).
Getting Started
Follow these steps to bring up the pipeline services and start processing data:
Navigate to the Project Directory:
Open a terminal and navigate to the root directory of your cloned repository, where your docker-compose.yml file is located.
Start Docker Compose Services:
Execute the following command to start all services defined in the docker-compose.yml file in detached mode:
docker-compose up -d

This command will download the necessary Docker images, create containers, and start the services.
Verify Services are Running:
Check the status of your services:
docker-compose ps

You should see all services listed as 'running'.
Configure Debezium Connector:
Once Kafka and Debezium are up, you will need to configure the Debezium PostgreSQL connector to start capturing changes from your PostgreSQL database. This typically involves sending a POST request to the Kafka Connect API.
(Example: You might have a create_connector.sh script or a connector-config.json file in your repository for this step.)
Start Flight Data Simulator:
Initiate your real-time flight data simulator to begin pushing data into the PostgreSQL database. This will trigger Debezium to capture changes.
Monitor Data Flow:
Observe the data flowing through Kafka (e.g., via Kafka consumer tools or Confluent Control Center if enabled) and then into your Snowflake tables.
Accessing Services (if applicable):
Kafka Control Center (if enabled): http://localhost:9021
Debezium UI (if enabled): http://localhost:8080
PostgreSQL: Accessible on its default port 5432 (or as configured in docker-compose.yml).
GitHub Workflow Automation
A dedicated GitHub workflow is implemented to connect to your Snowflake instance and execute SQL scripts. This workflow is specifically configured to trigger automatically whenever changes are pushed to the snowflake.sql file within the repository, ensuring that your Snowflake schema and data transformations are always up-to-date with your code.
Usage
Once the pipeline is operational:
Data Ingestion: The flight data simulator continuously feeds data into the system.
Real-time Processing: Debezium and Kafka ensure that changes are captured and streamed in near real-time.
Analytics: Data lands in Snowflake, ready for analytical queries, reporting, and dashboarding via tools like Power BI.
Consistency Checks: Rely on the automated GitHub Actions workflows to validate data consistency between PostgreSQL and Snowflake.
Customization
You can modify the docker-compose.yml file and other configuration files to suit your specific needs. For example:
Persist Data: Add volumes for PostgreSQL data to ensure data persistence across container restarts.
Resource Allocation: Adjust CPU and memory limits for containers.
Network Configuration: Customize network settings for inter-service communication.
Snowflake SQL: Modify the snowflake.sql file to update your Snowflake schema or introduce new transformations.
Shutting Down
To stop and remove the Docker containers, networks, and volumes created by Docker Compose, run:
docker-compose down


Note
This setup is primarily intended for development, testing, and demonstration purposes. For production environments, consider additional factors such as:
Security: Implement robust authentication, authorization, and network security.
Scalability: Design for high availability and horizontal scaling of Kafka, Debezium, and PostgreSQL.
Data Persistence: Ensure proper data backup and recovery strategies.
Monitoring & Alerting: Set up comprehensive monitoring with alerts for critical events.
Error Handling & Retries: Implement robust error handling and retry mechanisms throughout the pipeline.
🤝 Contributing
Contributions are welcome! If you have suggestions for improvements, bug fixes, or new features, please open an issue or submit a pull request.
📄 License
This project is open-source and available under the MIT License.
