from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class TicketForm(FlaskForm):
    current_city = StringField("Enter name of the city you will be leaving from", render_kw={"placeholder": "Enter An Origin"})
    destination_location = StringField("Enter the name of the city you want to go to", render_kw={"placeholder": "Enter A Destination"})
    leave = StringField("When do you plan on leaving: yy-mm", render_kw={"placeholder": "Start Date (yy-mm)"})
    returning = StringField("When do you plan on returning: yy-mm", render_kw={"placeholder": "Return Date (yy-mm)"})
    submit_button = SubmitField("Find Tickets For Me", render_kw={"onclick": "window.location.href='pricespage.html'"})