import Scripts.Database.database as db
import Scripts.Core.account as account

def tryLogin(username, password):
    if db.CheckPassword(username, password):
        account.name = username
        return True
    else:
        return False

def tryRegister(username, password):
    if db.DoesPlayerExist(username):
        return False
    db.AddNewPlayer(username, password)
    return True



