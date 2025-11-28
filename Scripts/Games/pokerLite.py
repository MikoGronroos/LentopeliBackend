import random

def Game(moneyToGamble):
    pList = []
    cList = []
    moneyWon = 0
    reRollCheck = [0,0,0,0,0,0]

    for i in range(5):
        pList.append(random.randint(1,9))
        cList.append(random.randint(3, 9))
    print("Welcome to Poker Lite!")
    print("""
              _____
             |A .  | _____
             | /.\ ||A ^  | _____
             |(_._)|| / \ ||A _  | _____
             |  |  || \ / || ( ) ||A_ _ |
             |____V||  .  ||(_'_)||( v )|
                    |____V||  |  || \ / |
                           |____V||  .  |
                                  |____V|
    """)
    print("RULES: You play against one opponent and are dealt 5 numbers \n"
          "You may choose to re-roll any numbers or keep your original hand \n"
          "Whoever has the higher hand after re-rolling wins.")
    print("")
    print(f"Your hand is: {pList}")

    while True:
        reRoll = int(input("What card do you want to re-roll? (select from cards 1-5 one at a time). When you're ready select 6 as input.) Re-roll: "))
        if reRoll == 6:
            break
        elif reRollCheck[reRoll] == 0:
            pList[reRoll] = random.randint(1, 9)
            reRollCheck[reRoll] = 1
            print(pList)

    print("")
    print(f"Your new hand is: {pList}")

    if sum(pList) > sum(cList):
        print(f"You won! Your total score was {sum(pList)} and the computer's was {sum(cList)}.")
        moneyWon = moneyToGamble * 2
    elif sum(pList) < sum(cList):
        print(f"You lost! Your total score was {sum(pList)} and the computer's was {sum(cList)}.")
    if sum(pList) == sum(cList):
        print(f"You tied with the computer! Your scores were {sum(pList)} .")
        moneyWon = moneyToGamble
    return moneyWon