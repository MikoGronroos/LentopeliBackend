import Scripts.Database.database as db
import Scripts.Core.account as account
import Scripts.Games.blackJack as blackjack
import Scripts.Games.russianRoulette as russianroulette
import Scripts.Games.noppaArvaus as noppa
import Scripts.Games.Roulette as roulette
import Scripts.Games.highCardLowCard as card
import Scripts.Games.pokerLite as poker
import os
import sys

games = {'AF': "",
         'AS': russianroulette.Game,
         'EU': poker.Game,
         'NA': roulette.Game,
         'SA': noppa.Game,
         'OC': card.Game}

def gamble():
    while True:
        if db.HasMoney(account.name) == False:
            print("You lost the game")
            sys.exit(0)
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"You have {db.GetPlayerMoney(account.name)} coins")
        amountToGamble = 0
        while True:
            amountToGamble = int(input("How much would you like to gamble? "))
            if db.CheckMoney(account.name, amountToGamble):
                break
        db.UpdateMoney(account.name, -amountToGamble)
        selectedGame = db.getPlayerContinent(account.name)
        game = games[selectedGame]
        moneyWon = game(amountToGamble)

        db.UpdateMoney(account.getGameId(), moneyWon)
        
        selection = int(input("1 to gamble and 2 to exit"))
        if selection == 1:
            os.system('cls' if os.name == 'nt' else 'clear')
        if selection == 2:
            return
