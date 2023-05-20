-- create  database hbtn_0d_usa and table cites (in the database hbtn_0d_usa)
-- in mysql server.
-- create database
CREATE DATABASE IF NIT EXISTS hbtn_0d_usa;
-- use database
USE hbtn_0d_usa;
-- create table
CREATE TABLE IF NOT EXISTS cities(id INT UNIQUE NOT NULL AUTO_INCREMENT,
state_id INT NOT NULL, name VARCHAR(256) NOT NULL, PRIMARY KEY(id),
FOREIGN KEY(state_id) REFERENCES states(id));
