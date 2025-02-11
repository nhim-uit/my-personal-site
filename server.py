# February 10, 2025
# My personal site - utilizing Flask
# Created by me (Alex Mai)

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
