from flask import Flask, redirect, url_for, render_template, request, session, flash
from flask_sqlalchemy import SQLAlchemy
import csv
import sqlite3


app = Flask(__name__)
app.config['SECRET_KEY'] = 'kinomania'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite'
db = SQLAlchemy(app)


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    passwordrepeat = db.Column(db.String(100), nullable=False)


class Films(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    title = db.Column(db.String(100), nullable=False)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/ფილმები')
def films():
    return render_template('Filmebi.html')


@app.route('/სერიალები')
def serialebi():
    return render_template('Serialebi.html')


@app.route('/ავტორიზაცია', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        session['username'] = username
        return redirect(url_for('user'))

    return render_template('Login.html')


@app.route('/მომხმარებელი')
def user():
    return render_template('User.html')


@app.route('/რეგისტრაცია', methods=['POST', 'GET'])
def register():
    if request.method=='POST':
        email = request.form['email']
        password = request.form['password']
        passwordrepeat = request.form['password-repeat']
        if email=='' or password=='' or passwordrepeat=='':
            flash('შეიტანეთ ყველა ველი', 'error')
        elif password != passwordrepeat:
            flash('სწორად შეიყვანეთ პაროლები', 'error')
        else:
            new_user = Users(email=email, password=password, passwordrepeat=passwordrepeat)
            db.session.add(new_user)
            db.session.commit()
            flash('დაემატა მომხმარებელი', 'info')

    return render_template('Create-account.html')

@app.route('/Logout')
def logout():
    session.pop('username')
    return render_template('index.html')


@app.route('/the_vault')
def the_vault():
    return render_template('the_vault.html')


@app.route('/interstellar')
def interstellar():
    return render_template('interstellar.html')


@app.route('/inception')
def inception():
    return render_template('inception.html')


@app.route('/Shawshenk_redemption')
def Shawshenk_redemption():
    return render_template('Shawshenk_redemption.html')


@app.route('/The_god_father')
def The_god_father():
    return render_template('/The-god-father.html')


@app.route('/The_dark_knight')
def The_dark_knight():
    return render_template('/dark-knight.html')


@app.route('/avangers_endgame')
def avangers_endgame():
    return render_template('avangers_endgame.html')


@app.route('/oops')
def oops():
    return render_template('oops.html')


@app.route('/lord_of_the_rings_the_return_of_the_king')
def lord_of_the_rings_the_return_of_the_king():
    return render_template('the-lords-of-the-rings-the-return-of-the-king.html')


@app.route('/თრეილერები')
def Trailer():
    return render_template('Trailers.html')


@app.route('/add_film', methods=['GET', 'POST'])
def add_film():
    if request.method == 'POST':
        t = request.form['title']
        u = request.form['username1']
        if t=='' or t=='':
            flash('შეიტანე ფილმის სახელი', 'error')
        elif u=='':
            flash('შეიყვანეთ თქვენი სახელი', 'error')
        else:
            Film = Films(title=t, username=u)
            db.session.add(Film)
            db.session.commit()
            flash('მონაცემები დამატებულია', 'info')

    return render_template('add_film.html')


@app.route('/ჩვენსშესახებ')
def chvensshesaxeb():
    return render_template('info_about_us.html')


@app.route('/კონტაქტი')
def contact():
    return render_template('contact.html')


@app.route('/ლეპტოპები')
def laptops():
    file = open('static/notebooks-information.csv', 'r', encoding='UTF-8')
    file_csv = file.readlines()
    all_notebooks = csv.reader(file_csv)

    return render_template('laptops.html', all_notebooks=all_notebooks)


if __name__ == "__main__":
    app.run(debug=True)