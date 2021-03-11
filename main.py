import flask
from flask import Flask


app = flask.Flask(__name__)

def get_latest_packages():
    return [
        {'name' : 'flask', 'version' : '1.2.3'},
        {'name': 'sqlalchmey', 'version': '2.2.0'},
        {'name': 'passlib', 'version': '3.0.0'},
    ]


@app.route('/')
def index():
    test_packages = get_latest_packages()
    return flask.render_template('index.html', packages = test_packages)


if __name__ == '__main__':
    app.run()

