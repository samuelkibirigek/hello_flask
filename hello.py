from flask import Flask

app = Flask(__name__)

@app.route("/bye")
def hello_world():
    return "<p>Hello, Worlds!</p>"

@app.route("/")
def say_bye():
    return "See you later!"

if __name__ == "__main__":
    app.run()

