--DROP TABLE ch_subscr; -- важна последовательность удаления таблиц!!

--DROP TABLE channel;
--DROP TABLE subscriber;


CREATE TABLE channel(
ch_id TEXT NOT NULL PRIMARY KEY,
username TEXT,
title TEXT
);

CREATE TABLE subscriber(
subscr_id INTEGER NOT NULL PRIMARY KEY,
username TEXT,
full_name TEXT
);

CREATE TABLE `ch_subscr` (
	`ch_subscr_id`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`ch_id`	TEXT NOT NULL,
	`subscr_id`	INTEGER NOT NULL,
	`username_ch` TEXT,
	`username_u` TEXT,
	`full_name` TEXT,
	FOREIGN KEY(`subscr_id`) REFERENCES `subscriber`(`subscr_id`) ON UPDATE CASCADE ON DELETE CASCADE,
	FOREIGN KEY(`ch_id`) REFERENCES `channel`(`ch_id`) ON UPDATE CASCADE ON DELETE CASCADE
);