from flask import Flask, request
from loginhelper import tryLogin, tryRegister

app = Flask(__name__)
@app.route('/login')
def login():
    username = request.args.get('username')
    password = request.args.get('password')

    if tryLogin(username, password) == True:
        return "Logged in successfully.."
    else:
        return "Wrong username or password.."

@app.route('/register')
def register():
    username = request.args.get('username')
    password = request.args.get('password')

    if tryRegister(username, password) == True:
        return "Registeration successful.."
    else:
        return "Username already exists.."

if __name__ == '__main__':
    app.run(debug=True)
    
