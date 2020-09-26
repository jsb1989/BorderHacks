from flask import Flask, render_template, request, url_for #Imports the flask framework.

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def homepage():
    return render_template('webpage.html')

if __name__ == 'main':
    app.run(debug=True)