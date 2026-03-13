CREATE DATABASE IF NOT EXISTS twitter_sentiment;

USE twitter_sentiment;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(100) NOT NULL UNIQUE,
    email VARCHAR(100),
    password VARCHAR(100)
);

CREATE TABLE inputs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    tweet TEXT,
    sentiment VARCHAR(20),
    FOREIGN KEY (user_id) REFERENCES users(id)
);