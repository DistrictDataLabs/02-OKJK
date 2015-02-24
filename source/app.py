from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
	return "Hallo friend"


@app.route("/cats")
def cats_hello():
	return "CATSSSSSS"

if __name__ == '__main__':
	app.run()