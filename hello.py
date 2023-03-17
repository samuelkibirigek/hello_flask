from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, Worlds!</p>"


@app.route("/bye")
def say_bye():
    return "<p>See you later!</p>"


if __name__ == "__main__":
    app.run()

