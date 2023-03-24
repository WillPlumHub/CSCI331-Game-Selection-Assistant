DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS collection;

CREATE TABLE user (
	id 			INTEGER NOT NULL,
	name 		TEXT UNIQUE NOT NULL,
    password 	TEXT NOT NULL,

    PRIMARY KEY (id)
);

CREATE TABLE game (
	id			INTEGER UNIQUE NOT NULL,
	name 		TEXT NOT NULL,
	playtime	INTEGER,

	PRIMARY KEY (id)
);

CREATE TABLE collection (
	gameId 		INTEGER NOT NULL,
	userId 		INTEGER NOT NULL,
	dateAdded	INTEGER NOT NULL,
	rating		INTEGER NOT NULL,

	FOREIGN KEY (userId) REFERENCES user(id),
	FOREIGN KEY (gameId) REFERENCES game(id),
	PRIMARY KEY (gameId, userId)
);
