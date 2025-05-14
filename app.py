from flask import Flask, render_template, request, redirect, url_for
from db import *


mycursor.execute("USE Pygame")

app = Flask(__name__)

@app.route('/')

def index():
    while True:
        mycursor.execute("SELECT * FROM USERS ORDER BY score DESC LIMIT 10")
        leaderboard = mycursor.fetchall()
        
        return render_template('index.html', leaderboard=leaderboard)




if __name__ == '__main__':
    app.run(debug=True)