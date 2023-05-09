from flask import Flask, render_template, request, jsonify, redirect
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')

    connect = sqlite3.connect('user-data.db')
    c = connect.cursor()
    c.execute("SELECT * FROM users WHERE username=? or email=?", (username, username))
    user = c.fetchone()
    print(user)

    c.execute("SELECT * FROM users WHERE (username=? or email=?) AND password=?", (username, username, password))
    user2=c.fetchone()

    if user:
        if user2:
            return redirect('/')
        else:
            token = 'JWT_TOKEN_HERE'
            return jsonify({ 'message': 'Incorrect Password!', 'token': token }), 401
    else:
        token = 'JWT_TOKEN_HERE'
        return jsonify({ 'message': 'Incorrect Username or Email!', 'token': token }), 401

@app.route('/signup', methods=['POST'])
def signup():
    first_name = request.json.get('first_name')
    last_name = request.json.get('last_name')
    email_id = request.json.get('email_id')
    mobile_number = request.json.get('mobile_number')
    username2 = request.json.get('username2')
    password2 = request.json.get('password2')
    dob = request.json.get('dob')

    print(username2, email_id)

    connect = sqlite3.connect('user-data.db')

    c = connect.cursor()
    c.execute("SELECT * FROM users WHERE username=?", (username2,))
    user = c.fetchone()

    c.execute("SELECT * FROM users WHERE email=?", (email_id,))
    user2=c.fetchone()

    if user:
        token = 'JWT_TOKEN_HERE'
        return jsonify({ 'message': 'Username Existed!', 'token': token }), 401
    else:
        if user2:
            print('hi')
            token = 'JWT_TOKEN_HERE'
            return jsonify({ 'message': 'Email Existed!', 'token': token }), 401
        else:
            c.execute('INSERT INTO user_details VALUES '+str((first_name, last_name, email_id, username2, password2, dob, mobile_number)))
            c.execute('INSERT INTO users VALUES '+str((email_id, username2, password2)))
            connect.commit()
            return redirect('/')

if __name__ == '__main__':
    app.run(port=5500, debug=True)
