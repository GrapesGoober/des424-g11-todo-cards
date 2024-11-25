-- init.sql will run automatically by the mysql container upon initialization automatically.
-- If you modified this init file, make sure to remove the volume mysqldata to force docker engine
-- to re-initialize the database.

CREATE DATABASE todocards;

USE todocards;

-- Just an example table to create
-- records texts to test API
CREATE TABLE text_records (
    `id` INTEGER PRIMARY KEY AUTO_INCREMENT,
    `text` TEXT
);

-- Deck
CREATE TABLE `deck` (
  `deckid` int(11) PRIMARY KEY AUTO_INCREMENT NOT NULL,
  `deckName` varchar(50) NOT NULL,
  `deckDescription` text NOT NULL,
  `deckOwnerID` varchar(50) NOT NULL
);

-- Deck-User
CREATE TABLE `access` (
  `deckid` int(11) NOT NULL,
  `userid` int(11) NOT NULL,
  `allow` BOOL DEFAULT FALSE,
  PRIMARY KEY (`deckid`, `userid`)
);

CREATE TABLE users (
    `username` VARCHAR(20) PRIMARY KEY,
    `password` TEXT,
    `date_of_birth` DATE,
    `email` TEXT
);