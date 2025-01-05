CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    hashed_password VARCHAR(255) NOT NULL,
    fitbit_user_id VARCHAR(255),
    fitbit_access_token VARCHAR(255),
    fitbit_refresh_token VARCHAR(255)
);