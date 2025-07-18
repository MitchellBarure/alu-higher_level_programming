-- A script that create the table force_name on your MySQL server

-- Create the table if it doesn't already exist
CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL
);
