-- Prepares a MySQL test server for the project

-- Creates the test db if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Creates the user if it doesn't exist
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- Grants all privileges on the test db to the created user
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

-- Grants select privilege to the created user on the performace_schema db
GRANT SELECT ON performace_schema.* TO 'hbnb_test'@'localhost';
