-- Prepares a MySQL dev server for the project

-- Creates the database if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Creates user if it doesn't exist
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- grants all privileges to the created user on the dev db
GRANT ALL PRIVILEGES ON hbnb_dev_db . * TO 'hbnb_dev'@'localhost';

-- grants select privileges to the created user on the performace_schema db
GRANT SELECT ON performace_schema . * TO 'hbnb_dev'@'localhost';
