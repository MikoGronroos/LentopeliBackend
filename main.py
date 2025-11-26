import Scripts.Core.gameLoop as gameLoop
import Scripts.Core.authentication as auth
import Scripts.Core.startNewGame as start
import Scripts.Database.database as db
import Scripts.Core.account as account

import os

#test

os.system('cls' if os.name == 'nt' else 'clear')

if auth.Authenticate():
    if db.isNewPlayer(account.name):
        start.startNewGame() 
    while True:
        gameLoop.GameLoop()
