USE DATABASE FLIGHTS;
USE SCHEMA PUBLIC;

CREATE TABLE IF NOT EXISTS my_test_table (
    id INT,
    name VARCHAR(255),
    created_at TIMESTAMP_NTZ DEFAULT CURRENT_TIMESTAMP()
);

INSERT INTO my_test_table (id, name) VALUES (1, 'Test Data');
INSERT INTO my_test_table (id, name) VALUES (2, 'Another Test');


