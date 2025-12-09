import mysql.connector
import random

yhteys = mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        database='flight_game',
        user='root',
        password='123456789',
        autocommit=True
        )

kursori = yhteys.cursor()

def DoesPlayerExist(name):
    sql = f'select * from game where screen_name = \'{name}\''
    kursori.execute(sql)
    return len(kursori.fetchall()) > 0

def GetPlayerMoney(name):
    sql = f'select money from game where screen_name = \'{name}\''
    kursori.execute(sql)
    return kursori.fetchone()[0]

def SetGambleStorage(id, money):
    sql = f"UPDATE game set gambleStorage = {money} where id = \'{id}\'"
    kursori.execute(sql)

def GetGambleStorage(id):
    sql = f"select gambleStorage from game where id = \'{id}\'"
    kursori.execute(sql)
    value = kursori.fetchall()[0]
    return value


def AddNewPlayer(name, password):
    sql = f"INSERT INTO game (id, location, password, screen_name, money, newPlayer) VALUES (%s, %s, %s, %s, %s, %s)"
    val = (random.randint(0,100000000), None, password, name, 100, True)
    kursori.execute(sql, val)

def CheckPassword(name, password):
    sql = f'select * from game where screen_name = \'{name}\' and password = \'{password}\''
    kursori.execute(sql)
    return len(kursori.fetchall()) > 0

def UpdateMoney(id, money):
    sql = f"UPDATE game set money = (money + {money}) where id = \'{id}\'"
    kursori.execute(sql)

def GetCurrentMoney(id):
    sql = f"select money from game where id = \'{id}\'"
    kursori.execute(sql)
    return kursori.fetchall()



def CheckMoney(name, money):
    sql = f"SELECT * FROM game where screen_name = \'{name}\' and money >= \'{money}\'"
    kursori.execute(sql)
    return len(kursori.fetchall()) > 0



def HasMoney(name):
    sql = f"SELECT * FROM game where screen_name = \'{name}\' and money > 0"
    kursori.execute(sql)
    return len(kursori.fetchall()) > 0

def fly(ident, name):
     sql = f"UPDATE game set location = \'{ident}\' where screen_name = \'{name}\'"   
     kursori.execute(sql)

def ResetPlayer(name):
    sql = f"UPDATE game set money = 100 where screen_name = \'{name}\'"   
    kursori.execute(sql)

def DeletePossibleAirports(id):
    sql = f"DELETE FROM possible_player_locations WHERE player_id = \'{id}\'"
    kursori.execute(sql)

def AddPossibleAirport(id, airport):
    sql = f"INSERT INTO possible_player_locations (player_id, location) VALUES (\'{id}\', \'{airport}\')"
    kursori.execute(sql)

def GetAllPossibleAirports(id):
    sql = f"SELECT * FROM possible_player_locations where player_id = \'{id}\'"
    kursori.execute(sql)
    return kursori.fetchall()

def GetAirport(icao):
    sql = f"SELECT * FROM airport where ident = \'{icao}\'"
    kursori.execute(sql)
    return kursori.fetchall()[0]

def GetCurrentPlayerAirport(id):
    sql = f"select location from game where id = \'{id}\'"
    kursori.execute(sql)
    return kursori.fetchall()

def getPlayerContinent(name):
    sql = f'select airport.continent from airport, game where game.screen_name = \'{name}\' and airport.ident = game.location' 
    kursori.execute(sql)
    return kursori.fetchall()
    
def getRandomAirportCode(continent):
    sql = f"SELECT ident FROM airport where continent = '{continent}' and type = 'large_airport'" 
    kursori.execute(sql)
    newList = kursori.fetchall()
    return newList[random.randint(0, len(newList))][0]

def isNewPlayer(name):
    sql = f'select * from game where screen_name = \'{name}\' and newPlayer = true'
    kursori.execute(sql)
    return len(kursori.fetchall()) > 0

def newPlayerCreated(location, name):
    sql = f"UPDATE game set location = \'{location}\', newPlayer = 0 where screen_name = \'{name}'"
    kursori.execute(sql)


def airportTaker(continent):
    countryList = []
    sql = f"SELECT name, latitude_deg, longitude_deg, continent, ident FROM airport where continent = '{continent}' and type = 'large_airport'" 
    kursori.execute(sql)
    result = kursori.fetchall()
    randomInt = random.randint(0, kursori.rowcount - 1)
    countryList.append(result)
    return result[randomInt]

def takeAllAirports(): 
    continentList = ["EU", "AS", "NA", "SA", "AF", "OC"]
    airportList = []
    for i in range(len(continentList)):
        airportList.append(airportTaker(continentList[i]))
    return airportList

def getGameId(name):
    kursori.execute(f"select id from game where screen_name = \'{name}'")
    id = kursori.fetchall()[0][0]
    return id

def getPostcardId(continent):
    kursori.execute(f"SELECT id FROM postcards WHERE continent =  \'{continent}'")
    postcard = kursori.fetchone()
    if not postcard:
        return
    postcard_id = postcard[0]
    return postcard_id

def alreadyHasPostcard(player_id, continent):
    value = getPostcardId(continent)
    sql = f"select * from player_postcards where postcard_id = \'{value}\' and player_id = \'{player_id}\'"

    kursori.execute(sql)
    return len(kursori.fetchall()) > 0

def getAllPostcards():
    sql = f"SELECT * FROM postcards"
    kursori.execute(sql)
    return kursori.fetchall()


def playerHasAllPostcards(player_id):
    sql = f"SELECT * FROM player_postcards where player_id = \'{player_id}\'"
    kursori.execute(sql)
    return len(kursori.fetchall()) >= 6


def collect_postcard(player_id, postcard_id):
    val = (player_id, postcard_id)
    sql = "INSERT IGNORE INTO player_postcards (player_id, postcard_id) VALUES (%s, %s)"

    kursori.execute(sql, val)

def show_collected_postcards(player_id):
    kursori.execute(f"select postcards.name, postcards.continent from player_postcards, postcards where player_id =  \'{player_id}' and postcards.id = player_postcards.postcard_id")
    return kursori.fetchall()

def addVoucher(player_id):
    sql = f"UPDATE game SET vouchers = vouchers + 1 WHERE id = {player_id}"
    kursori.execute(sql)

def GetWeatherForAirport(icao):
    sql = f"SELECT temperature, wind, clouds FROM weather WHERE ident = '{icao}'"
    kursori.execute(sql)
    result = kursori.fetchone()

    if not result:
        return None

    return {
        "temperature": result[0],
        "wind": result[1],
        "clouds": result[2]
    }
