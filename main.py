from flask import Flask

app = Flask(__name__)

@app.route('/')
def homepage():
    return 'Hello, world!'

#this prints 'Hello, world!' onto a blank page :)
#new test dfas main

if __name__ == '__main__':
    app.run()

