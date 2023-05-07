from flask import Flask
import requests
import json

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello, Dapr!"


@app.route("/greeting")
def get_state():

    # Get the current value for key "mystate"
    count_url = "http://localhost:8089/v1.0/state/statestore/mystate"
    count_response = requests.get(count_url)
    count = count_response.text

    if count == '':
        count = 1
    else:
        count = int(count) + 1

    # Update mystate value
    stateObj = [{"Key": "mystate", "Value": count}]
    stateData = json.dumps(stateObj).encode("utf-8")
    headers = {"Content-Type": "application/json"}
    resp = requests.post(
        "http://localhost:8089/v1.0/state/statestore", data=stateData, headers=headers)

    return f"Greetings! You are visitor number {count}."
