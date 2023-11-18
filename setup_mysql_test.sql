-- Prepares a MySQL test server for the project

CREATE IF NOT EXISTS DATABASE hbnb_test_db;
CREATE IF NOT EXISTS USER 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
GRANT SELECT ON performace_schema.* TO 'hbnb_test'@'localhost';
