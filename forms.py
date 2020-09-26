from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired


class ticket_form(FlaskForm):
    current_city = StringField("Enter name of the city you will be leaving from", InputRequired())
    destination_location = StringField("Enter the name of the city you want to go to", InputRequired())
    leave = StringField("When do you plan on leaving: yy-mm", InputRequired())
    returning = StringField("When do you plan on returning: yy-mm", InputRequired())
    submit_button = SubmitField("Find Tickets For Me")