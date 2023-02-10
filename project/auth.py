from flask import Blueprint, render_template, request, url_for,session, redirect
from . import app
from project.models import user, db
import re

@app.route("/ins/")
def ins():
    return render_template("Inscription.html")

@app.route("/connect/")
def connect():
    return render_template("login.html")

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method =='POST' and 'email' in request.form and 'password' in request.form:
        email=request.form.get('email')
        password=request.form.get('password')
        remember= True if request.form.get('remember') else False
        account= user.query.filter_by(email=email).first()
        if account:
            message='Vous etes maintenant connecter!'
            return render_template('user.html',message= message)
        else:
            message= 'Mot de passe ou email incorrect!'
            return render_template('login.html', message=message)

@app.route('/inscrit', methods=['GET','POST'])
def inscrit():
    if request.method =='POST' and 'name' in request.form and 'pnom' in request.form and 'password' in request.form and 'email' in request.form:
        userName= request.form['name']
        pnom=request.form['pnom']
        password=request.form['password']
        email=request.form['email']
        password2= request.form['password2']
        account= user.query.filter_by(email=email).first()
        if account:
            message='Vous etes déjà inscrit!'
        elif not userName or not pnom or not password or not email:
            message='Formulaire non remplis!'
        elif password!=password2:
            message='Erreur de confirmation!'
        else:
            new_account=user(name=userName, pnom=pnom,email=email, password=password)
            db.session.add(new_account)
            db.session.commit()
            message='Félicitation! Vous etes maintenant inscrit! '
            return render_template('login.html', message=message)
            
    elif request.method == 'POST':
        message='Formulaire non remplis!'
    return render_template('Inscription.html',message= message)




if __name__=="__main__":
    app.run(debug=True)