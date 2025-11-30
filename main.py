import Scripts.Core.gameLoop as gameLoop
import Scripts.Core.authentication as auth
import Scripts.Core.startNewGame as start
import Scripts.Database.database as db
import Scripts.Core.account as account
from flask import Flask, request, jsonify
app = Flask(__name__)

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
