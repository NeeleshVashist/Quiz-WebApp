from flask import Flask, flash, redirect, render_template, request, session, abort
import os

app = Flask(__name__)
app.secret_key = 'some secret key'


@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return render_template('welcome.html')


@app.route('/login', methods=['POST'])
def do_admin_login():
    if request.form['password'] == 'secret' and request.form['username'] == 'admin':
        session['logged_in'] = True
    else:
        flash('wrong password!')
    return home()


@app.route("/logout")
def logout():
    session['logged_in'] = False
    return home()


@app.route('/welcome')
def welcome():
    return render_template('welcome.html')


@app.route('/template')
def template():
    return render_template('first_page.html')


@app.route('/quiz')
def quiz():
    return render_template('quiz.html')


if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True, host='0.0.0.0', port=4000)
