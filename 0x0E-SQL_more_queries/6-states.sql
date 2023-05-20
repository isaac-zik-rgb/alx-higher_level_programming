-- create the database htbn_0d_usa and a table states in the databse hbtn_0d_usa on MYSQL server
-- description: id INT UNIQUE, AUTO INCREMENT NOT NULL PRIARY KEY name VARCHAR(256)
-- create the database hbtn_0d_usa
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- use the database
USE hbtn_0d_usa;
-- create table
CREATE TABLE IF NOT EXISTS `states`(id INT UNIQUE AUTO INCREMENT NOT NULL PRIMARY KEY, name VARCHAR(256));
