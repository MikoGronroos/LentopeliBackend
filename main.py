import Scripts.Core.gameLoop as gameLoop
import Scripts.Core.authentication as auth
import Scripts.Core.startNewGame as start
import Scripts.Database.database as db
import Scripts.Core.account as account
from flask import Flask, request, jsonify
from Scripts.Core.travel import travel
from Scripts.Core.loginflask import auth
from Scripts.Core.server import shop
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    app.register_blueprint(travel)
    app.register_blueprint(auth)

    app.register_blueprint(shop)
    return app

app = create_app()
CORS(app)

if __name__ == "__main__":
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
