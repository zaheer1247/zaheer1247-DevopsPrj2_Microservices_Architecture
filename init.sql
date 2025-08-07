-- CREATE DATABASE users;

-- \c users

-- Create the users table if it does not exist
-- Insert initial data into the users table, ignoring conflicts on the name field
-- This ensures that if the user already exists, it will not be inserted again
-- This is useful for development and testing purposes to ensure the table has some data
-- The table has three columns: id (primary key), name (unique), and info (text about the user)
-- The id is an auto-incrementing serial number
-- The name is a unique text field that cannot be null
-- The info is a text field that cannot be null and contains information about the user
-- The initial data includes three users: Alice, Bob, and Ram with their respective info
-- The ON CONFLICT clause ensures that if a user with the same name already exists, the insert will not fail
-- This allows the script to be run multiple times without causing errors due to duplicate entries
-- The script is idempotent, meaning it can be run multiple times without changing the result beyond the initial application
-- This is useful for setting up a development environment or testing database
 
CREATE TABLE IF NOT EXISTS usersdata (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL UNIQUE,
    info TEXT NOT NULL
);

INSERT INTO usersdata (name, info) VALUES
('Amit', 'Software engineer from Bangalore'),
('Priya', 'Data analyst working in Mumbai'),
('Rahul', 'Graphic designer based in Delhi'),
('Sneha', 'Marketing specialist focused on social media in Hyderabad'),
('Rajesh', 'Cybersecurity expert and ethical hacker from Pune')
ON CONFLICT (name) DO NOTHING;
