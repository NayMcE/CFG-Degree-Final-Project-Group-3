import mysql.connector
from jinja2.utils import Joiner


import pymysql


from config import USER, PASSWORD, HOST, DATABASE



class DbConnectionError(Exception):
    pass

#connect database to PyGame
def _db_connection():
    try:
        cnx = pymysql.connect(
            host = HOST,
            user = USER,
            password = PASSWORD,
            database = DATABASE
        )

        cursor = cnx.cursor()
        return cnx, cursor
    except pymysql.MySQLError as e:
        raise DbConnectionError(f"Database connection error: {e}")

#function to save player details to database
def save_player_details(character_name):
    query = "INSERT INTO player (player_character) VALUES (%s)"
    cursor.execute(query, (character_name,))
    db.commit()


#function to save items player collected
def save_player_items(item_name):
    query = "INSERT INTO items (item_name) VALUES (%s)"
    cursor.execute(query, (item_name,))
    db.commit()


#function to save players movements
def save_player_actions(action_name):
    query = "INSERT INTO actions (action_name) VALUES (%s)"
    cursor.execute(query, (action_name,))
    db.commit()


#function with join query to display player stats
def fetch_player_stats():
    query = """
    SELECT 
        p.player_character,
        COUNT(s.item_id) AS teacups_collected,
        SUM(CASE WHEN a.action_name = "Climbed ladder" THEN 1 ELSE 0 END) AS ladders_climbed,
        SUM(CASE WHEN a.action_name = "Fell in rabbit hole" THEN 1 ELSE 0 END) AS rabbit_holes_fell_down
    FROM
        player p
    LEFT JOIN
        stats s ON p.player_id = s.player_id
    LEFT JOIN
        items i ON s.item_id = i.item_id
    LEFT JOIN
        actions a ON s.action_id = a.action_id
    GROUP BY
        p.player_id, p.player_character; 
    """
    cursor.execute(query)
    return cursor.fetchall()


def close_connection():
    cursor.close()
    db.close()


if __name__ == '__main__':
    _db_connection()
    save_player_details()
    save_player_items()
    save_player_actions()
    fetch_player_stats()