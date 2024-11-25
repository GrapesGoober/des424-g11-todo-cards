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

-- User
CREATE TABLE users (
    `username` VARCHAR(20) PRIMARY KEY,
    `password` TEXT,
    `date_of_birth` DATE,
    `email` TEXT
);

-- Deck
CREATE TABLE deck (
  `deckid` int(11) PRIMARY KEY AUTO_INCREMENT NOT NULL,
  `deckName` varchar(50) NOT NULL,
  `deckDescription` TEXT NOT NULL,
  `deckOwnerName` varchar(20) NOT NULL,
  FOREIGN KEY (deckOwnerName) REFERENCES users(username) ON DELETE CASCADE
);

-- Deck-User
CREATE TABLE access (
  `deckid` int(11) NOT NULL,
  `username` varchar(20) NOT NULL,
  `allow` BOOL DEFAULT FALSE,
  PRIMARY KEY (`deckid`, `username`),
  FOREIGN KEY (deckid) REFERENCES deck(deckid) ON DELETE CASCADE,
  FOREIGN KEY (username) REFERENCES users(username) ON DELETE CASCADE
);