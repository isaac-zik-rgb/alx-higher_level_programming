-- Create a database hbtn_0d_usa and table states in htbn_0d_usa database
-- create database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- use database.
USE hbtn_0d_usa;
-- Create table
CREATE TABLE IF NOT EXISTS `states`(`id` INT UNIQUE NOT NULL AUTO INCREMENT, `name` VARCHAR(256) NOT NULL, PRIMARY KEY(id));
