from tokenize import String
from wsgiref.validate import validator
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField, SelectField, RadioField, TextAreaField
from wtforms.validators import InputRequired, Length, ValidationError, DataRequired, Optional
from app.models import Users

class RegisterForm(FlaskForm):
    firstName = StringField(validators=[InputRequired(), Length(min=1, max=50)], render_kw={"placeholder": "First Name"})
    lastName = StringField(validators=[InputRequired(), Length(min=1, max=50)], render_kw={"placeholder": "Last Name"})
    username = StringField(validators=[InputRequired(), Length(min=4, max=50)], render_kw={"placeholder": "Username"})
    password = PasswordField(validators=[InputRequired(), Length(min=8, max=40)], render_kw={"placeholder": "Password"})
    age = IntegerField(validators=[InputRequired()], render_kw={"placeholder":"Age"})
    gender = SelectField(validators=[InputRequired()],choices=[("Male"),("Female")])
    preference = SelectField(validators=[InputRequired()],choices=[("Male"),("Female")])
    bio = TextAreaField(validators=[InputRequired(), Length(min=100, max=600)], render_kw={"placeholder": "Bio: Minimum 100 characters"})
    email = StringField(validators=[InputRequired(), Length(min=3, max=50)], render_kw={"placeholder": "Email"})
    
    submit = SubmitField("Register")
    
    def userValidation(self, username):
        existingUser = Users.query.filter_by(username=username.data).first()
        if existingUser:
            raise ValidationError("That username is taken. Please choose a different one!")
        
class LoginForm(FlaskForm):
    username = StringField(validators=[InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Username"})
    password = PasswordField(validators=[InputRequired(), Length(min=8, max=40)], render_kw={"placeholder": "Password"})
    
    submit = SubmitField("Login")
    
    def __repr__(self):
        return '<Name %r>' %self.id

    def to_json(self):
        return {
            "firstName":self.firstName,
            "lastName":self.lastName,
            "age":self.age,
            "gender":self.gender,
            "preference":self.preference,
            "bio":self.bio,
            "email":self.email,
            "username":self.username,
            "password":self.password   
        }
class MatchForm(FlaskForm):
    email = StringField(validators=[DataRequired()])

class MessageForm(FlaskForm):
    message = TextAreaField("Message", render_kw={"placeholder": "Send a message..."})