from flask import Flask, request, jsonify
from loginhelper import tryLogin, tryRegister
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if tryLogin(username, password) == True:
        return jsonify({"message": "Logged in successfully.."})
    else:
        return jsonify({"message": "Wrong username or password.."})

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    print(username, password)
    if tryRegister(username, password) == True:
        return jsonify({"message": "Registeration successful.."})
    else:
        return jsonify ({"message": "Username already exists.."})

if __name__ == '__main__':
    app.run(debug=True)
    
