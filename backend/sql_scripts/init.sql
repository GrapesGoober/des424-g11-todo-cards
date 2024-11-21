-- init.sql will run automatically by the mysql container upon initialization automatically.
-- If you modified this init file, make sure to remove the volume mysqldata to force docker engine
-- to re-initialize the database.

CREATE DATABASE todocards;

-- Just an example table to create
CREATE TABLE text_records (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    text TEXT
);
