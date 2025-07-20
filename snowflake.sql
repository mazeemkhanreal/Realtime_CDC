USE DATABASE FLIGHTS;
USE SCHEMA PUBLIC;

CREATE TABLE IF NOT EXISTS test_table (
    id INT,
    name VARCHAR(255),
    created_at TIMESTAMP_NTZ DEFAULT CURRENT_TIMESTAMP()
);

INSERT INTO test_table (id, name) VALUES (1, 'Test Data');
INSERT INTO test_table (id, name) VALUES (2, 'Another Test');


