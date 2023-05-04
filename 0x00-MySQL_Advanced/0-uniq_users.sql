-- creates a table users with:
    -- id, integer, never null, auto increment and primary key
    -- email, string (255 characters), never null and unique
    -- name, string (255 characters)
CREATE TABLE IF NOT EXISTS users(
    id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    name VARCHAR(255)
);
