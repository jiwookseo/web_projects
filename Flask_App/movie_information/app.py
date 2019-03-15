from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timezone, timedelta
from save2csv import load_csv
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data/movies.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
db = SQLAlchemy(app)
db.init_app(app)

class Movie(db.Model):
    __tablename__='movies'
    id=db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String, nullable=False, unique=True)
    title_en=db.Column(db.String, nullable=False)
    audience=db.Column(db.Integer, nullable=False)
    open_date=db.Column(db.DateTime, nullable=False)
    genre=db.Column(db.String, nullable=False)
    watch_grade=db.Column(db.String, nullable=False)
    score=db.Column(db.Float, nullable=False)
    poster_url=db.Column(db.Text, nullable=False)
    description=db.Column(db.Text, nullable=False)
    
db.create_all()

@app.route('/movies')
def index():
    sort_by=request.args.get("sort")
    if sort_by=='2':
        movies=Movie.query.order_by(Movie.open_date.desc()).all()
    elif sort_by=='3':
        movies=Movie.query.order_by(Movie.audience.desc()).all()
    elif sort_by=='4':
        movies=Movie.query.order_by(Movie.score.desc()).all()
    else:
        movies=Movie.query.all()
    return render_template('index.html',movies=movies)
    # <option value="1">Boxoffice (Default)</option>
    # <option value="2">Open Date</option>
    # <option value="3">Audience</option>
    # <option value="4">User Rate</option>
    
@app.route('/movies/new')
def new():
    return render_template('new.html')
    
@app.route('/movies/create', methods=["POST"])
def create():
    title=request.form.get('title')
    title_en=request.form.get('title_en')
    audience=request.form.get('audience')
    open_date=datetime.strptime(request.form.get('open_date'),'%Y-%m-%d')
    genre=request.form.get('genre')
    watch_grade=request.form.get('watch_grade')
    score=request.form.get('score')
    poster_url=request.form.get('poster_url')
    description=request.form.get('description')
    a=Movie(title=title,title_en=title_en,audience=audience,open_date=open_date,genre=genre,watch_grade=watch_grade,score=score,poster_url=poster_url,description=description)
    db.session.add(a)
    db.session.commit()
    a=Movie.query.filter_by(title=title).first()
    pk=a.id
    return redirect('/movies/{}'.format(pk))
    
@app.route('/movies/<int:pk>')
def show(pk):
    movie=Movie.query.get(pk)
    return render_template('show.html',movie=movie)
    
@app.route('/movies/<int:pk>/edit')
def edit(pk):
    movie=Movie.query.get(pk)
    return render_template('edit.html',movie=movie)
    
@app.route('/movies/<int:pk>/delete')
def delete(pk):
    movie=Movie.query.get(pk)
    db.session.delete(movie)
    db.session.commit()
    return redirect('/movies')
    
@app.route('/movies/<int:pk>/update', methods=["POST"])
def update(pk):
    movie=Movie.query.get(pk)
    movie.title=request.form.get('title')
    movie.title_en=request.form.get('title_en')
    movie.audience=request.form.get('audience')
    movie.open_date=datetime.strptime(request.form.get('open_date'),'%Y-%m-%d')
    movie.genre=request.form.get('genre')
    movie.watch_grade=request.form.get('watch_grade')
    movie.score=request.form.get('score')
    movie.poster_url=request.form.get('poster_url')
    movie.description=request.form.get('description')
    db.session.commit()
    return redirect('/movies/{}'.format(pk))
    
@app.route('/movies/load')
def load():
    data=load_csv('data/data.csv')
    for row in data:
        a=Movie(title=row[0],title_en=row[1],audience=row[2],open_date=datetime.strptime(row[3],'%Y%m%d'),genre=row[4],watch_grade=row[5],score=row[6],poster_url=row[7],description=row[8])
        db.session.add(a)
    db.session.commit()
    return redirect('/movies')