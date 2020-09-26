from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class TicketForm(FlaskForm):
    current_city = StringField("Enter name of the city you will be leaving from", )
    destination_location = StringField("Enter the name of the city you want to go to",)
    leave = StringField("When do you plan on leaving: yy-mm",)
    returning = StringField("When do you plan on returning: yy-mm", )
    submit_button = SubmitField("Find Tickets For Me")