from os import environ
from flask import Flask, render_template
#import SQLALchemy
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
#set the SQLALCHEMY_DATABASE_URI key
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///my_database.db'
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DATABASE_URL').replace("://", "ql://", 1) or 'sqlite:///myDB.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'you-will-never-guess'
#create an SQLAlchemy object named `db` and bind it to your app
db = SQLAlchemy(app)
#a simple initial greeting
from models import User,Song,Item,Playlist
db.create_all()


@app.route('/')
@app.route('/index')
def greeting():
    return render_template('greeting.html')

# app name 
@app.errorhandler(404) 
def not_found(e): 
  return render_template("404.html") 

#uncomment the code below here when you are done creating database instance db and models
import routes

# try:
#     p1 = Playlist(id = 1)
#     p2 = Playlist(id = 2)
#     p3 = Playlist(id = 3)
#     p4 = Playlist(id = 4)
#     u1 = User(id = 1, username = "mlky_way", playlist_id = p1.id)
#     u2 = User(id = 2, username = "martian2", playlist_id = p2.id)
#     u3 = User(id = 3, username = "andromeda_3", playlist_id = p3.id)
#     u4 = User(id = 4, username = "calypso123", playlist_id = p4.id)

#     s1 = Song(id = 1, artist = "Franks Sinatra", title = "Fly me to the Moon", n = 0)
#     s2 = Song(id = 2, artist = "David Bowie", title = "Space Oddity", n = 0)
#     s3 = Song(id = 3, artist = "Sting", title = "Walking on the Moon", n = 0)
#     s4 = Song(id = 4, artist = "Nick Cave & The Bad Seeds", title = "Rings of Saturn", n = 0) 
#     s5 = Song(id = 5, artist = "Babylon Zoo", title = "Spaceman", n = 0)

#     db.session.add(p1)
#     db.session.add(p2)
#     db.session.add(p3)
#     db.session.add(p4)
#     db.session.add(u1)
#     db.session.add(u2)
#     db.session.add(u3)
#     db.session.add(u4)
#     db.session.add(s1)
#     db.session.add(s2)
#     db.session.add(s3)
#     db.session.add(s4)
#     db.session.add(s5)
#     db.session.commit()

# except:
#     pass
