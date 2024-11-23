CREATE database game_storage;

USE game_storage;

CREATE table player
(
player_id int NOT NULL AUTO_INCREMENT,
player_name VARCHAR(200) NOT NULL,
CONSTRAINT pk_player_id PRIMARY KEY (player_id)
);

CREATE table items
(
item_id int NOT NULL,
item_name VARCHAR(200) NOT NULL,
CONSTRAINT pk_item_id PRIMARY KEY (item_id)
);

CREATE table player_collection
(
player_collection_id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
player_id int NOT NULL,
item_id int NOT NULL,
CONSTRAINT pk_player FOREIGN KEY (player_id)
REFERENCES player(player_id),
CONSTRAINT pk_items_collected FOREIGN KEY (item_id)
REFERENCES items(item_id)
);

INSERT INTO items (item_id, item_name)
VALUES
("1", "Mad Hatters Hat"),
("2", "Cup of tea")
;