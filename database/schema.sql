DROP DATABASE IF EXISTS brawl; 

CREATE DATABASE brawl;

\c brawl;

CREATE TABLE brawler (
    brawler_id INT GENERATED ALWAYS AS IDENTITY,
    brawler_version SMALLINT NOT NULL,
    brawler_name TEXT NOT NULL,
    created_at DATETIME NOT NULL,
    updated_at DATETIME NOT NULL,
    PRIMARY KEY (brawler_id)
);

CREATE TABLE starpower (
    starpower_id SMALLINT GENERATED ALWAYS AS IDENTITY,
    starpower_version SMALLINT NOT NULL,
    brawler_id INT NOT NULL,
    brawler_version SMALLINT NOT NULL,
    starpower_name TEXT NOT NULL,
    created_at DATETIME NOT NULL,
    updated_at DATETIME NOT NULL,
    PRIMARY KEY (starpower_id),
    FOREIGN KEY (brawler_id) REFERENCES brawler (brawler_id),
    FOREIGN KEY (brawler_version) REFERENCES brawler (brawler_version)
);

CREATE TABLE gear (
    gear_id SMALLINT GENERATED ALWAYS AS IDENTITY,
    gear_version SMALLINT NOT NULL,
    brawler_id INT NOT NULL,
    brawler_version SMALLINT NOT NULL,
    gear_name TEXT NOT NULL,
    created_at DATETIME NOT NULL,
    updated_at DATETIME NOT NULL,
    PRIMARY KEY (gear_id),
    FOREIGN KEY (brawler_id) REFERENCES brawler (brawler_id),
    FOREIGN KEY (brawler_version) REFERENCES brawler (brawler_version)
);