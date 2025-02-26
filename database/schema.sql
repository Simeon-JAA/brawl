DROP DATABASE IF EXISTS brawl; 

CREATE DATABASE brawl;

\c brawl;
CREATE TABLE brawler (
    id SMALLINT GENERATED ALWAYS AS IDENTITY,
    brawler_id INT NOT NULL,
    brawler_version SMALLINT NOT NULL,
    brawler_name TEXT NOT NULL,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    PRIMARY KEY (brawler_id, brawler_version)
);

CREATE TABLE starpower (
    id SMALLINT GENERATED ALWAYS AS IDENTITY,
    starpower_id INT NOT NULL,
    starpower_version SMALLINT NOT NULL,
    brawler_id INT NOT NULL,
    brawler_version SMALLINT NOT NULL,
    starpower_name TEXT NOT NULL,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    PRIMARY KEY (starpower_id, starpower_version),
    FOREIGN KEY (brawler_id, brawler_version) REFERENCES brawler (brawler_id, brawler_version)
);

CREATE TABLE gatdget (
    id SMALLINT GENERATED ALWAYS AS IDENTITY,
    gatdget_id INT NOT NULL,
    gatdget_version SMALLINT NOT NULL,
    brawler_id INT NOT NULL,
    brawler_version SMALLINT NOT NULL,
    gatdget_name TEXT NOT NULL,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    PRIMARY KEY (gatdget_id, gatdget_version),
    FOREIGN KEY (brawler_id, brawler_version) REFERENCES brawler (brawler_id, brawler_version)
    );

CREATE TABLE gear (
    id SMALLINT GENERATED ALWAYS AS IDENTITY,
    gear_id INT NOT NULL,
    gear_version SMALLINT NOT NULL,
    brawler_id INT NOT NULL,
    brawler_version SMALLINT NOT NULL,
    gear_name TEXT NOT NULL,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    PRIMARY KEY (gear_id, gear_version),
    FOREIGN KEY (brawler_id, brawler_version) REFERENCES brawler (brawler_id, brawler_version)
    );
