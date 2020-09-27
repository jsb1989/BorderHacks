from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, validators
from wtforms.validators import DataRequired


class TicketForm(FlaskForm):
    current_city = StringField("Enter name of the city you will be leaving from",
                               render_kw={"placeholder": "Enter An Origin"}, validators=[DataRequired()])
    destination_location = StringField("Enter the name of the city you want to go to",
                                       render_kw={"placeholder": "Enter A Destination"}, validators=[DataRequired()])
    #leave = StringField("When do you plan on leaving: yy-mm", render_kw={"placeholder": "Start Date (yy-mm)"})
    leave = DateField("Departure Date ", format="%y-%m", render_kw={"placeholder": "Start Date (yy-mm)"},
                      validators=[DataRequired()])
    returning = DateField("Returning Date ", format="%y-%m", render_kw={"placeholder": "Returning Date (yy-mm)"},
                          validators=[DataRequired()])
    submit_button = SubmitField("Find Tickets For Me", render_kw={"onclick": "window.location.href='pricespage.html'"},
                                validators=[DataRequired()])