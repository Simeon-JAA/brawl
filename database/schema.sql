DROP DATABASE IF EXISTS brawl; 

CREATE DATABASE brawl;

\c brawl;
CREATE TABLE brawler (
    brawler_id INT NOT NULL,
    brawler_version SMALLINT NOT NULL,
    brawler_name TEXT NOT NULL,
    created_at DATETIME NOT NULL,
    updated_at DATETIME,
    PRIMARY KEY (brawler_id, brawler_version)
);

CREATE TABLE starpower (
    starpower_id INT NOT NULL,
    starpower_version SMALLINT NOT NULL,
    brawler_id INT NOT NULL,
    brawler_version SMALLINT NOT NULL,
    starpower_name TEXT NOT NULL,
    created_at DATETIME NOT NULL,
    updated_at DATETIME,
    PRIMARY KEY (starpower_id, starpower_version),
    FOREIGN KEY (brawler_id) REFERENCES brawler (brawler_id),
    FOREIGN KEY (brawler_version) REFERENCES brawler (brawler_version)
);

CREATE TABLE gear (
    gear_id INT NOT NULL,
    gear_version SMALLINT NOT NULL,
    brawler_id INT NOT NULL,
    brawler_version SMALLINT NOT NULL,
    gear_name TEXT NOT NULL,
    created_at DATETIME NOT NULL,
    updated_at DATETIME,
    PRIMARY KEY (gear_id, gear_version),
    FOREIGN KEY (brawler_id) REFERENCES brawler (brawler_id),
    FOREIGN KEY (brawler_version) REFERENCES brawler (brawler_version)
);
