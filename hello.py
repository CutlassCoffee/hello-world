from flask import Flask

app = Flask(__name__)

@app.route('/<person>')
def hello(person):
    return '<strong>Hello</strong>, %s!' % person
