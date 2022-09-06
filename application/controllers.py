from flask import Flask
from flask import render_template,redirect, url_for
from flask import request
from application.database import db
from application.models import User
from application.models import Decks
from application.models import Cards
from flask import current_app as app

import csv
from io import StringIO
from flask import make_response

# login page
@app.route("/" , methods=["GET","POST"])
def login_page():
    if request.method=="GET":
        return render_template("login.html")
    elif request.method=="POST":
        id=0
        user_name=request.form["user_name"]
        password=request.form["password"]
        email=request.form["email"]
        users=db.session.query(User).all()
        l=[]
        for u in users:
            l.append(u.name)
        #sign up
        if request.form["Go"]=="Sign Up":
            if user_name not in l:
                us = User(name=user_name, password=password,email=email)
                db.session.add(us)
                db.session.flush()
                db.session.commit()
                return redirect(url_for('dash',id=str(us.user_id)))
            else:
                return render_template("login.html",warning="* username already exists.")
        #log in
        elif request.form["Go"]=="Log In":
            if user_name in l:
                for j in users:
                    if user_name == j.name:
                        id=j.user_id
                        print(id)
                print(str(id))
                return redirect(url_for('dash',id=str(id)))
            else:
                return render_template("login.html",warning="* username does not exists.")
        db.session.close_all()
    else:
        print("Error ")


@app.route("/dashboard/<id>",methods=["GET","POST"])
def dash(id):
    if request.method=="GET": 
        return render_template("dashboard.html")
    elif request.method == "POST":
        if request.form["Go"]=="add_deck":
            return redirect(url_for('add',id=id))
        elif request.form["Go"]=="view_decks":
            return redirect(url_for('view',id=id))
       
@app.route("/dashboard/deck_form/<id>",methods=["GET","POST"])
def add(id):
    if request.method=="GET":
        return render_template("deck_form.html")
    elif request.method=="POST":
        deck_name=request.form["deck_name"]
        decks=Decks.query.filter(Decks.user_id==id).all()
        l=[]
        for d in decks:
            l.append(d.deck_name)
        if deck_name not in l:
            deck=Decks(deck_name=deck_name,user_id=id)
            db.session.add(deck)
            db.session.flush()
            db.session.commit()
            db.session.close_all()
            return render_template("deck_form.html",warning="* deck created")
        else:
            return render_template("deck_form.html",warning="* deck has to be unique")

@app.route("/dashboard/deck_table/<id>",methods=["GET","POST"])
def view(id):
    decks=Decks.query.filter(Decks.user_id==id).all()
    if request.method=="GET":
        return render_template("deck_table.html",decks=decks)
    elif request.method=="POST":
        if request.form["Go"]=="view":
            return redirect(url_for('view_card',id=id))
        elif request.form["Go"]=="edit":
            return redirect(url_for('edit_decks',id=id))
        elif request.form["Go"]=="update":
            return redirect(url_for('update',id=id))
        elif request.form["Go"]=="export_decks":
            si = StringIO()
            cw = csv.writer(si)
            records = Decks.query.filter(Decks.user_id==id).all()
            cw.writerows([(r.deck_id, r.deck_name, r.score) for r in records])
            response = make_response(si.getvalue())
            response.headers['Content-Disposition'] = 'attachment; filename=decks.csv'
            response.headers["Content-type"] = "text/csv"
            return response
        

@app.route("/dashboard/update/<id>",methods=["GET","POST"])
def update(id):
    if request.method=="GET":
        return render_template("update_deck.html")
    elif request.method=="POST":
        old_name=request.form["old_name"]
        new_name=request.form["new_name"]
        decks=Decks.query.filter(Decks.user_id==id).all()
        deck_id=0
        for d in decks:
            if d.deck_name==old_name:
                deck_id=d.deck_id
        db.session.query(Decks).filter(Decks.deck_id==deck_id).update(dict(deck_name=new_name))
        db.session.commit()
        return redirect(url_for("view",id=id))



@app.route("/daashboard/edit_decks/<id>",methods=["GET","POST"])
def edit_decks(id):
    if request.method=="GET":
        return render_template("edit_deck.html")
    elif request.method=="POST":
        delete_deck=request.form["deck_name"]
        deck=request.form["deck"]
        ques=request.form["ques"]
        ans=request.form["ans"]
        decks=Decks.query.filter(Decks.user_id==id).all()
        l=[]
        for d in decks:
            l.append(d.deck_name)
        #delete_deck
        if request.form["Go"]=="delete_deck":
            if delete_deck not in l:
                return render_template("edit_deck.html",warning_delete="* deck is not present")
            else:
                deck_id=0
                for d in decks:
                    if d.deck_name==delete_deck:
                        deck_id=d.deck_id
                Decks.query.filter_by(deck_id=deck_id).delete()
                db.session.commit()
                return redirect(url_for('view',id=id))
        #add card
        elif request.form["Go"]=="add_card":
            print(deck)
            print(deck not in l)
            if deck not in l:
                return render_template("edit_deck.html",warning_deck="* deck not present")
            else:
                deckId=0
                for d in decks:
                    if d.deck_name==deck:
                        deckId=d.deck_id
                cards=Cards.query.filter(Cards.deck_id==deckId).all()
                l=[]
                for c in cards:
                    l.append(c.ques)
                if ques in l:
                    return render_template("edit_deck.html",warning_card="* card is already present")
                else:
                    card=Cards(ques=ques,ans=ans,deck_id=deckId)
                    db.session.add(card)
                    db.session.flush()
                    db.session.commit()
                    return render_template("edit_deck.html",warning="* card created")

        elif request.form["Go"]=="delete_card":
            if deck not in l:
                return render_template("edit_deck.html",warning_deck="* deck is not present")
            else:
                deckId=0
                for d in decks:
                    if d.deck_name==deck:
                        deckId=d.deck_id
                cards=Cards.query.filter(Cards.deck_id==deckId).all()
                l=[]
                for c in cards:
                    l.append(c.ques)
                if ques not in l:
                    return render_template("edit_deck.html",warning="* card is not present")
                else:
                    cardId=0
                    for c in cards:
                        if c.ques==ques:
                            cardId=c.card_id
                    Cards.query.filter_by(card_id=cardId).delete()
                    db.session.commit()
                    return render_template("edit_deck.html",warning="* card deleted")
        elif request.form["Go"]=="back":
            return redirect(url_for("view",id=id))
               
@app.route("/dashboard/view_card/<id>",methods=["GET","POST"])
def view_card(id):
    if request.method=="GET":
        return render_template("view_card.html")
    elif request.method=="POST":
        decks=Decks.query.filter(Decks.user_id==id).all()
        deck=request.form["deck_name"]
        l=[]
        for d in decks:
            l.append(d.deck_name)
        deckId=0
        for d in decks:
            if d.deck_name==deck:
                deckId=d.deck_id
        if request.form["Go"]=="back":
            return redirect(url_for('view',id=id))
        elif request.form["Go"]=="view":
            if deck not in l:
                return render_template("view_card.html",warning="* no such deck")
            else:
                cards=Cards.query.filter(Cards.deck_id==deckId).all()
                if len(cards)==0:
                    return render_template("view_card.html",warning="* no cards to view")
                else:
                    return redirect(url_for('card',deck_id=deckId))
        elif request.form["Go"]=="export_cards":
            si = StringIO()
            cw = csv.writer(si)
            records = Cards.query.filter(Cards.deck_id==deckId).all()
            cw.writerows([(r.card_id, r.ques, r.ans) for r in records])
            response = make_response(si.getvalue())
            response.headers['Content-Disposition'] = 'attachment; filename=cards.csv'
            response.headers["Content-type"] = "text/csv"
            return response
        

c_id=[]
score=0 
count=0   
@app.route("/dashboard/cards/<deck_id>",methods=["GET","POST"])
def card(deck_id):
    global c_id
    global count
    global score
    cards=Cards.query.filter(Cards.deck_id==deck_id).all()
    decks=db.session.query(Decks).all()
    user_id=0
    for d in decks:
        if d.deck_id==deck_id:
            user_id=d.user_id
    if not c_id:
        for c in cards:
            c_id.append(c.card_id)
    
    ques=""
    ans=""
    id=c_id[0]
    for i in cards:
        if i.card_id==id:
            ques=i.ques
            ans=i.ans
    if request.method=="GET":
        return render_template("cards.html",question=ques)
    if request.method=="POST":
        if request.form["score"]:
            score = score + int(request.form["score"])
        print(score)
        if request.form["Go"]=="answer":
            return render_template("cards.html",question=ques,answer=ans)
        if request.form["Go"]=="next":
            c_id=c_id[1:]
            count=count+1
            print(count)
            average=0
            if count==len(cards):
                average=score/len(cards)
                db.session.query(Decks).filter(Decks.deck_id==deck_id).update(dict(score=average))
                db.session.commit()
                return redirect(url_for('view',id=user_id))
            else:
                return redirect(url_for('card',deck_id=deck_id))