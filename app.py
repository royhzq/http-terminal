from flask import Flask, request, jsonify, render_template, session, redirect, url_for
from utils import exec
from settings import TERMINAL_KEY

app = Flask(__name__)
app.secret_key = "secretkey"

@app.route('/terminal/auth', methods=['GET', 'POST'])
def terminal_authentication():

    if request.method == "POST":
        user_key = request.form.get('password')
        if user_key == TERMINAL_KEY:
            session['TERMINAL_KEY'] = user_key
            return redirect(url_for('.view_terminal'))
        else:
            return redirect(url_for('.terminal_authentication'))

    return render_template('terminal_authentication.html')

@app.route('/terminal')
def view_terminal():

    if session.get('TERMINAL_KEY') != TERMINAL_KEY:
        return redirect(url_for('.terminal_authentication'))

    return render_template('terminal.html')


@app.route('/command', methods=['GET','POST'])
def send_command():

    data = request.json
    command = data.get('command')
    if command:
        stdout, stderr = exec(command)
    else:
        stdout, stderr = [], []
    resp = {
        'stdout':stdout,
        'stderr':stderr
    }
    return jsonify(resp)

if __name__ == '__main__':
    app.run(host='0.0.0.0')