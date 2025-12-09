import Scripts.Database.database as db

name = ""
continent = ""
airport = ""
   
def getGameId():
    return db.getGameId(name)
