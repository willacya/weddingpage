from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, \
    TextAreaField, IntegerField, DecimalField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, \
    Length

class RSVPForm(FlaskForm):
    username = StringField('Name', validators=[DataRequired()])
    email = StringField('Email')
    message = TextAreaField('Message', validators=[DataRequired()])
    submit = SubmitField('Send Message')