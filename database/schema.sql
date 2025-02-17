DROP DATABASE IF EXISTS brawl; 

CREATE DATABASE brawl;

\c brawl;

CREATE TABLE brawler (
    brawler_id SMALLINT GENERATED ALWAYS AS IDENTITY,
    brawler_name TEXT NOT NULL,
    brawler_version SMALLINT NOT NULL,
    created_at DATETIME NOT NULL,
    updated_at DATETIME NOT NULL,
    PRIMARY KEY (brawler_id)
);