import os
import Scripts.Database.database as db
import Scripts.Core.account as account
import sys

def shop():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"Here you can buy the postcard from {db.getPlayerContinent(account.name)} for 25 coins")
        selection = int(input("1 to buy, 2 to exit: "))
        if selection == 1:
            if db.CheckMoney(account.name, 25):
                check = db.alreadyHasPostcard(account.getGameId(), db.getPlayerContinent(account.name)) 
                if check == False:
                    print("You bought the postcard")
                    value = db.getPostcardId(db.getPlayerContinent(account.name))
                    db.collect_postcard(account.getGameId(), value)
                    db.UpdateMoney(account.getGameId(), -25)
                else:
                    print("You already have this postcard")
            else:
                print("Not enough coins")
            if db.playerHasAllPostcards(account.getGameId()):
                print("You won the game!")
                sys.exit(0)
            else:
                input("Press enter to continue")

        if selection == 2:
            return
