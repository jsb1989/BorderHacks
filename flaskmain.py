from flask import Flask, render_template, request, url_for # Imports the flask framework.
from flask_bootstrap import Bootstrap
from . forms import TicketForm

app = Flask(__name__)
app.secret_key = "SECRET"
Bootstrap(app)

@app.route('/', methods=("GET", "POST"))
@app.route('/home', methods=("GET", "POST"))
def homepage():
    ticketform = TicketForm()
    return render_template('webpage.html', form=ticketform)


if __name__ == 'main':
    app.run(debug=True)