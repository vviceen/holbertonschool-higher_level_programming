-- script that creates the database and the table in the database
CREATE DATANASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states(
    id INT NOT NULL AUTO_INCREMENT UNIQUE,
    PRIMARY KEY (id)
    name VARCHAR(256) NOT NULL
);