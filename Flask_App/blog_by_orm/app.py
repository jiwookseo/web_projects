from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timezone, timedelta
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data/blog2.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
db = SQLAlchemy(app)
db.init_app(app)

def time():
    tz=timezone(timedelta(hours=9))
    dt = datetime.now(tz)
    return dt.strftime("%H:%M, %A %d. %B %Y")
    
class Article(db.Model):
    __tablename__ = "articles"
    id=db.Column(db.Integer, primary_key=True, autoincrement=True)
    title=db.Column(db.String, nullable=False)
    content=db.Column(db.String, nullable=False)
    author=db.Column(db.String, nullable=False)
    created_at=db.Column(db.String, nullable=False)

db.create_all()

@app.route('/articles')
def main():
    articles=Article.query.all()
    return render_template('main.html',articles=articles)
    
@app.route('/articles/<pk>')
def article(pk):
    article = Article.query.get(pk)
    return render_template('article.html',article=article)

@app.route('/articles/new')
def new():
    return render_template('new.html')
    
@app.route('/articles/create', methods=["POST"])
def submit():
    title=request.form.get('title')
    content=request.form.get('content')
    author=request.form.get('author')
    created_at=time()
    a=Article(title=title,content=content,author=author,created_at=created_at)
    db.session.add(a)
    db.session.commit()
    article=Article.query.filter_by(title=title,content=content,author=author,created_at=created_at).first()
    pk=article.id
    return redirect('articles/{}'.format(pk))
    
@app.route('/articles/<pk>/delete')
def delete(pk):
    article = Article.query.get(pk)
    db.session.delete(article)
    db.session.commit()
    return redirect('/articles')

@app.route('/articles/<pk>/edit')
def edit(pk):
    article = Article.query.get(pk)
    return render_template('edit.html',article=article)

@app.route('/articles/<pk>/update',methods=["POST"])
def update(pk):
    article = Article.query.get(pk)
    article.content=request.form.get("content")
    article.title=request.form.get("title")
    article.author=request.form.get("author")
    article.created_at=time()
    db.session.commit()
    return redirect('articles/{}'.format(pk))