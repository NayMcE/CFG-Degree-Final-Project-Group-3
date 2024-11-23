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
("1", "Mad Hatters Hat"),
("2", "Cup of tea")
;


INSERT INTO actions (action_id, action_name)
VALUES
("1", "Climbed ladder"),
("2", "Fell in rabbit hole")
;


-- JOIN TO DISPLAY PLAYER NAME, ITEMS COLLECTED AND HOW MANY LADDERS CLIMBED/RABBIT HOLES FALLEN INTO

SELECT
    p.player_name,
    COUNT(DISTINCT s.item_id) AS items_collected,
    SUM(CASE WHEN a.action_name = 'Climbed ladder' THEN 1 ELSE 0 END) AS ladders_climbed,
    SUM(CASE WHEN a.action_name = 'Fell in rabbit hole' THEN 1 ELSE 0 END) AS rabbit_holes_fell_down
FROM
    player p
LEFT JOIN
    stats s ON p.player_id = s.player_id
LEFT JOIN
    items i ON s.item_id = i.item_id
LEFT JOIN
    actions a ON s.action_id = a.action_id
GROUP BY
    p.player_id, p.player_name;