-- This is your postgres.sql file
-- Add your SQL commands here. For example:

USE DATABASE MY_DATABASE;
USE SCHEMA MY_SCHEMA;

CREATE TABLE IF NOT EXISTS my_test_table (
    id INT,
    name VARCHAR(255),
    created_at TIMESTAMP_NTZ DEFAULT CURRENT_TIMESTAMP()
);

INSERT INTO my_test_table (id, name) VALUES (1, 'Test Data');
INSERT INTO my_test_table (id, name) VALUES (2, 'Another Test');

SELECT * FROM my_test_table;

-- You can add any DDL or DML statements here.
