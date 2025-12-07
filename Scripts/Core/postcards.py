import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="salasana",
    database="luontiscript"
)
cursor = conn.cursor()

def collect_postcard(player_id, continent):
    cursor.execute("SELECT id FROM postcards WHERE continent = %s", (continent,))
    postcard = cursor.fetchone()
    if not postcard:
      return
    postcard_id = postcard[0]
    cursor.execute("INSERT IGNORE INTO player_postcards (player_id, postcard_id) VALUES (%s, %s)", (player_id, postcard_id))
    conn.commit()

def show_collected_postcards(player_id):
    cursor.execute("""
        SELECT p.continent, p.name
        FROM postcards p
        JOIN player_postcards pp ON p.id = pp.postcard_id
        WHERE pp.player_id = %s
    """, (player_id,))
    for continent, name in cursor.fetchall():
        print(f"{name} ({continent})")

player_id = int(input("Player ID: "))
continents = ["Europe", "Asia", "Africa", "North America", "South America", "Australia"]

for c in continents:
    collect_postcard(player_id, c)

show_collected_postcards(player_id)

cursor.close()
conn.close()
