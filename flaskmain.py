from flask import Flask, render_template, request, url_for, redirect # Imports the flask framework.
from flask_bootstrap import Bootstrap
from . forms import TicketForm

app = Flask(__name__)
app.secret_key = "SECRET"
Bootstrap(app)

@app.route('/', methods=("GET", "POST"))
@app.route('/home', methods=("GET", "POST"))
def homepage():
    ticketform = TicketForm()
    if request.method == "POST":
        return redirect(url_for('pricespage'))
    return render_template('webpage.html', form=ticketform)


@app.route('/prices', methods=("GET", "POST"))
def pricespage():
    return render_template('pricespage.html')

if __name__ == 'main':
    app.run(debug=True)