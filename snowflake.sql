-- The file is commented out so this is not run in our snowflake instance, as we have already set everything up.
/*
USE ROLE SECURITYADMIN;

CREATE ROLE KAFKA_CONNECTOR_ROLE
    COMMENT = 'Role for Snowflake Kafka Connector to ingest data.';

CREATE USER kafka_connector_user
RSA_PUBLIC_KEY='X' -- Paste the cleaned public key here
DEFAULT_ROLE = KAFKA_CONNECTOR_ROLE
DEFAULT_WAREHOUSE = YOUR_WAREHOUSE_NAME -- Replace with your actual warehouse name
COMMENT = 'User for Snowflake Kafka Connector authentication.';

GRANT ROLE KAFKA_CONNECTOR_ROLE TO USER kafka_connector_user;

USE ROLE SYSADMIN;

-- Create or replace database flights;
CREATE DATABASE FLIGHTS;

-- Grant usage on your target database
GRANT USAGE ON DATABASE FLIGHTS TO ROLE KAFKA_CONNECTOR_ROLE;

-- Grant usage on your target schema
GRANT USAGE ON SCHEMA FLIGHTS.PUBLIC TO ROLE KAFKA_CONNECTOR_ROLE;

-- Grant privileges needed to create/manage objects for the connector:
GRANT CREATE TABLE ON SCHEMA FLIGHTS.PUBLIC TO ROLE KAFKA_CONNECTOR_ROLE;
GRANT CREATE STAGE ON SCHEMA FLIGHTS.PUBLIC TO ROLE KAFKA_CONNECTOR_ROLE;
GRANT CREATE PIPE ON SCHEMA FLIGHTS.PUBLIC TO ROLE KAFKA_CONNECTOR_ROLE;
GRANT INSERT ON ALL TABLES IN SCHEMA FLIGHTS.PUBLIC TO ROLE KAFKA_CONNECTOR_ROLE;

-- Grant usage on the warehouse (so the connector can use compute resources)
GRANT USAGE ON WAREHOUSE COMPUTE_WH TO ROLE KAFKA_CONNECTOR_ROLE;
GRANT OPERATE ON WAREHOUSE COMPUTE_WH TO ROLE KAFKA_CONNECTOR_ROLE; 


alter user kafka_connector_user set rsa_public_key='-----BEGIN PUBLIC KEY----------END PUBLIC KEY-----';




-- Script to check for latency
with temp_table as (
select 
TO_TIMESTAMP((record_metadata:CreateTime)::string) snowflake_created_at,
TO_TIMESTAMP(((record_content:payload):after):inserted_at::string) postgres_created_at,
datediff(millisecond,postgres_created_at ,snowflake_created_at) millisecond_lag
from flights.public.cdc_public_flights_2113051958
)
select 
count(*) as total_records,
avg(millisecond_lag) lag_in_milliseconds,
avg(millisecond_lag)/1000 lag_in_seconds from temp_table;


*/
