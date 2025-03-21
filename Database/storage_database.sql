CREATE database storage_database;


USE storage_database;


CREATE table player
(
player_id int NOT NULL AUTO_INCREMENT,
player_character VARCHAR(200) NOT NULL,
CONSTRAINT pk_player_id PRIMARY KEY (player_id),
CONSTRAINT uq_player_character UNIQUE (player_character)
);


CREATE table items
(
item_id int NOT NULL,
item_name VARCHAR(200) NOT NULL,
CONSTRAINT pk_item_id PRIMARY KEY (item_id)
);


CREATE table actions
(
action_id int NOT NULL,
action_name VARCHAR(200) NOT NULL,
CONSTRAINT pk_action_id PRIMARY KEY (action_id)
);


CREATE table stats
(
stats_id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
player_id int NOT NULL,
item_id int NOT NULL,
action_id int NOT NULL,
CONSTRAINT pk_player_stats FOREIGN KEY (player_id)
REFERENCES player(player_id),
CONSTRAINT pk_items_collected FOREIGN KEY (item_id)
REFERENCES items(item_id),
CONSTRAINT pk_actions_taken FOREIGN KEY (action_id)
REFERENCES actions(action_id)
);



INSERT INTO items (item_id, item_name)
VALUES
("1", "Teacup")
;

INSERT INTO actions (action_id, action_name)
VALUES
("1", "Climbed ladder"),
("2", "Fell in rabbit hole")
;


INSERT INTO player (player_character)
VALUES
("Alice"),
("Cheshire Cat"),
;
