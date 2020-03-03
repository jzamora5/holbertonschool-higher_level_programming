-- Creates the table id_not_null on your MySQL server.
-- Query to perform operation
CREATE TABLE IF NOT EXISTS unique_id (
       id INT DEFAULT 1 UNIQUE,
       name VARCHAR(256)
);
