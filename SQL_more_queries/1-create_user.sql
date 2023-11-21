-- Script to create a new user in MySQL and grant all privileges

-- Create the user 'user_0d_1' with the specified password if it does not exist
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- Grant all privileges to 'user_0d_1' on all databases and tables
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;

-- Apply the changes made by the GRANT statement
FLUSH PRIVILEGES;