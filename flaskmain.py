from flask import Flask, render_template, request, url_for #Imports the flask framework.

app = Flask(__name__)

if __name__ == 'main':
    app.run(debug=True)