import Scripts.Core.gameLoop as gameLoop
import Scripts.Core.authentication as auth
import Scripts.Core.startNewGame as start
import Scripts.Database.database as db
import Scripts.Core.account as account
from flask import Flask, request, jsonify
from Scripts.Core.startNewGame import startGame
from Scripts.Core.travel import newAirports
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    app.register_blueprint(startGame)
    app.register_blueprint(newAirports)
    return app

app = create_app()
CORS(app)

@app.route('/', methods=['GET'])
def works():
    return "Hei"

if __name__ == "__main__":
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
