from flask import Flask
import os
app = Flask(__name__)
app.run(debug=True)


@app.route('/')
def hello_world():
    return 'Hello, my v1 version docker images! ' + os.getenv("HOSTNAME") + ''
