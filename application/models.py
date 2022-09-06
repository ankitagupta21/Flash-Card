from .database import db
from sqlalchemy.orm.relationships import foreign
from sqlalchemy.sql.schema import ForeignKey

class User(db.Model):
    __tablename__='Users'
    user_id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(30))
    password=db.Column(db.String(300))
    email=db.Column(db.String(300))

    def __int__(self,name,password):
        self.name=name
        self.password=password

class Decks(db.Model):
    __tablename__='decks'
    deck_id=db.Column(db.Integer,primary_key=True)
    deck_name=db.Column(db.String(30))
    user_id=db.Column(db.Integer,db.ForeignKey("Users.user_id"))
    score=db.Column(db.Integer)

class Cards(db.Model):
    __tablename__='card'
    deck_id=db.Column(db.Integer,db.ForeignKey("decks.deck_id"))
    card_id=db.Column(db.Integer,primary_key=True)
    ques=db.Column(db.String(1000))
    ans=db.Column(db.String(1000))
