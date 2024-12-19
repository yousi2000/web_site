from flask import Flask, jsonify, render_template, request
import os


app = Flask(__name__)


app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlKihBXox7C0sKR6b'
app.config['SECRET_KEY'] = os.environ.get('FLASK_KEY')
@app.route("/")
def home():
    return render_template("index.html")




if __name__ == '__main__':
    app.run(debug=True)
