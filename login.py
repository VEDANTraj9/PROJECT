from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dummy user database (Replace this with your actual user database)
users = {
    "user1": "password1",
    "user2": "password2"
}

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    if username in users and users[username] == password:
        # Successful login
        return redirect(url_for('success'))
    else:
        # Failed login
        return redirect(url_for('failure'))

@app.route('/success')
def success():
    return "Login Successful!"

@app.route('/failure')
def failure():
    return "Login Failed!"

if __name__ == '__main__':
    app.run(debug=True)
