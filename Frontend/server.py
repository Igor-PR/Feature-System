from flask import Flask
from flask import render_template
import sys

app = Flask(__name__)

@app.route('/', )
def index():
    return render_template('index.html')

@app.route('/clientproductareas')
def clientproductareas():
    return render_template('clientProductAreas.html')

@app.route('/features')
def features():
    return render_template('features.html')

@app.route('/about')
def about():
    return render_template('about.html')                    

if __name__ == "__main__":
    app.run()
