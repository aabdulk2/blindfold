from flask import Flask, request, render_template, redirect, url_for, Blueprint
from flask_login import UserMixin, LoginManager, login_required, login_user, logout_user, current_user
from app.forms import LoginForm, RegisterForm
from app.forms.user_forms import MatchForm, MessageForm
from app.models import Users, db
import random
from werkzeug.security import generate_password_hash, check_password_hash
from faker import Faker
from app.models.Matches import Matches
from app.models.Messages import Messages

fake = Faker()

auth_routes = Blueprint("auth", __name__)

def get_my_matches():
    your_likes = Matches.query.filter(Matches.userid_Matching == current_user.id).all()
    liked_you = Matches.query.filter(Matches.userid_Matched == current_user.id).all()
    your_likes_ids = [user.userid_Matched for user in your_likes]
    liked_you_ids = [user.userid_Matching for user in liked_you]
    
    def intersection(l1, l2):
        return list(set(l1) & set(l2))
    
    your_matches = intersection(your_likes_ids, liked_you_ids)
    
    users = []
    for userid in your_matches:
        user = Users.query.get(userid)
        users.append(user)
    return users    

def get_msgs(their_id):
    our_msgs_unfiltered = current_user.messages
    our_msgs = [message for message in our_msgs_unfiltered if message.userid_received == their_id]
    their_user = Users.query.get(their_id)
    their_msgs = their_user.messages
    user_msgs = our_msgs + their_msgs
    def sortbyid(message):
        return message.id
    user_msgs.sort(key=sortbyid)
    return user_msgs

@auth_routes.route("/profile", methods=['GET','POST'])
@login_required
def outputProfile():
    return render_template("profile.html",user=current_user)

@auth_routes.route('/logout', methods=['GET','POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth_routes.route("/home")
@login_required
def homePage():
    return render_template("home.html",user=current_user)

@auth_routes.route("/login",methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = Users.query.filter_by(username=form.username.data).first()
        print('\n\n')
        print(user)
        print('\n\n')
        if user:
            if check_password_hash(user.password, form.password.data):
                login_user(user)
                return redirect(url_for('auth.outputProfile'))
            
    return render_template('login.html', form=form)
    
@auth_routes.route("/register",methods=['GET','POST'])
def registerPage():
    form = RegisterForm()
    print('\n\n')
    print(form.validate_on_submit())
    print(form.data)
    print('\n\n')
    if form.validate_on_submit():
        hashedPass = generate_password_hash(form.password.data)
        print("\\n",hashedPass,"\n\n")
        newUser = Users(
            username=form.username.data, 
            password=hashedPass, 
            firstName=form.firstName.data, 
            lastName=form.lastName.data, 
            age=form.age.data, 
            bio=form.bio.data,
            gender=form.gender.data, 
            preference=form.preference.data, 
            email=form.email.data
        )
        db.session.add(newUser)
        db.session.commit()
        return redirect(url_for('auth.login'))
        
    return render_template('register.html', form=form)

@auth_routes.route("/match",methods=['GET'])
def findMatch():
    users = Users.query.all()
    random_user = random.choice(users)
    while random_user == current_user:
        random_user = random.choice(users)
        
    return render_template("match.html",user=random_user)

@auth_routes.route("/matched", methods=["POST"])
def match():
    form = MatchForm()
    print(form.data)
    user_liked = Users.query.filter(Users.email == form.email.data).first()
    print(user_liked.id)
    sent_like = Matches(userid_Matched=user_liked.id,userid_Matching=current_user.id)
    db.session.add(sent_like)
    db.session.commit()
    received_like = Matches.query.filter(Matches.userid_Matching == user_liked.id and Matches.userid_Matched == current_user.id).first()
    if received_like:
        return f"You and {user_liked.firstName} both matched!"
    return form.data



@auth_routes.route("/matches", methods=["GET"])
def matches():
    users = get_my_matches()
    
    for user in users:
        print(user.firstName)    
        
    return render_template("matches.html",users=users,user=current_user)


@auth_routes.route("/message/<int:userid_received>", methods=["POST"])
def message(userid_received):
    form = MessageForm()
    new_message = Messages(
        userid_received=userid_received,
        userid_sent=current_user.id,
        message=form.message.data
    )
    db.session.add(new_message)
    db.session.commit()
    
    print("\n\n",current_user.messages,"Over here")
    allusers = get_my_matches()
    all_messages = get_msgs(userid_received)
    print("\n\n", all_messages)
    user = Users.query.get(userid_received)
    
    return render_template("matches.html",users=allusers,user=user,messages=all_messages)

@auth_routes.route("/messages/<int:our_id>/<int:their_id>")
def get_users_messages(our_id,their_id):
    messages = get_msgs(their_id)
    allusers = get_my_matches()
    user = Users.query.get(their_id)
    return render_template("matches.html",users=allusers,user=user,messages=messages)

@auth_routes.route("/matches/<int:userid>", methods=["GET"])
def get_user_msg(userid):
    user = Users.query.get(userid)
    messages = get_msgs(userid)
    allusers = get_my_matches()
    return render_template("matches.html",user=user,users=allusers,messages=messages)

@auth_routes.route("/seedall")
def seed_all():
    for i in range(100):
        user = Users(
            username= fake.user_name(), 
            password=generate_password_hash("password"), 
            firstName=fake.first_name(), 
            lastName=fake.last_name(), 
            age=fake.pyint(18,60), 
            bio=fake.paragraph(nb_sentences=7),
            gender=random.choice(["Male","Female"]), 
            preference=random.choice(["Male","Female"]), 
            email=fake.email()
        )
        db.session.add(user)
        db.session.commit()
    return "Seeded"