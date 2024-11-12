import urllib.parse, urllib.request, urllib.error, json, flask

from flask import Flask
app = Flask(__name__)
@app.route("/")
def is_it_raining_in_seattle():
    with urllib.request.urlopen('https://depts.washington.edu/ledlab/teaching/is-it-raining-in-seattle/') as response:
        is_it_raining_in_seattle = response.read().decode()

    if is_it_raining_in_seattle == "true":
        return "<p>Yes</p>"
    else:
        return "<p>No</p>"

if __name__ == "__main__":
    app.run(debug=True)