from flask import Flask
from helloworld import *
import os

app = Flask(__name__)

@app.route("/")
def home():
    return helloworld()
	
@app.route("/webhook")
def update():
    git = os.popen("git pull")
    output = git.read()
    return output