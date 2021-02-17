from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
	return 'Hello Paulo!'

@app.route('/apelido')
def hello_world():
	return 'Hello Serafim!'
