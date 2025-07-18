-- This script creates the table unique_id on your MySQL server
-- Create the table if it doesn't already exist
CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);
