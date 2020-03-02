-- Displays the number of records with id = 89 in the table first_table of the database
-- Query to create table
CREATE TABLE IF NOT EXISTS second_table (
       id INT,
       name VARCHAR(256),
       score INT
);
-- Query to insert values
INSERT INTO second_table
       (id, name, score)
VALUES
	(1, "John", 10),
	(2, "Alex", 3),
	(3, "Bob", 14),
	(3, "George", 8);
