from flask import Flask, render_template, request, redirect
import sqlite3
from datetime import datetime, timezone, timedelta

app=Flask(__name__)
DB_FILE='data/blog.db'
DB_TABLE='articles'

def query(method, table, *params):
    c=sqlite3.connect(DB_FILE)
    db=c.cursor()
    check=True
    method=method.lower()
    if method=='select_all':
        q='SELECT * FROM {}'.format(table)
    elif method=='select_one':
        q='SELECT * FROM {} WHERE id={}'.format(table,params[0])
    elif method=='select_id':
        q='SELECT id FROM {} WHERE title="{}" and content="{}" and author="{}" order by id DESC limit 1'.format(table,*params)
    elif method=='create':
        q='INSERT INTO {} (title, content, author, created_at) VALUES ("{}","{}","{}","{}")'.format(table, *params)
    elif method=='update':
        q='UPDATE {} SET title="{}", content="{}", author="{}", created_at="{}" WHERE id="{}"'.format(table, *params)
    elif method=='delete':
        q='DELETE FROM {} WHERE id="{}"'.format(table, *params)
    if method=='select_all' or method=='select_one' or method=='select_id':
        check=False
    db.execute(q)
    if check:
        c.commit()
        c.close()
        return None
    else:
        data=db.fetchall()
        c.close()
        return data

def time():
    tz=timezone(timedelta(hours=9))
    dt = datetime.now(tz)
    return dt.strftime("%H:%M, %A %d. %B %Y")

@app.route('/articles')
def main():
    data=query('select_all',DB_TABLE)
    return render_template('main.html',data=data)
    
@app.route('/articles/<pk>')
def article(pk):
    data=query('select_one',DB_TABLE,pk)
    return render_template('article.html',data=data)

@app.route('/articles/new')
def new():
    return render_template('new.html')
    
@app.route('/articles/create', methods=["POST"])
def submit():
    title=request.form.get('title')
    content=request.form.get('content')
    author=request.form.get('author')
    created_at=time()
    query('create',DB_TABLE,title,content,author,created_at)
    data=query('select_id',DB_TABLE,title,content,author)
    print(data)
    pk=data[0][0]
    return redirect('articles/{}'.format(pk))
    
@app.route('/articles/<pk>/delete')
def delete(pk):
    query('DELETE',DB_TABLE,pk)
    return redirect('/articles')

@app.route('/articles/<pk>/edit')
def edit(pk):
    data=query('select_one',DB_TABLE,pk)
    return render_template('edit.html',data=data)

@app.route('/articles/<pk>/update',methods=["POST"])
def update(pk):
    edit_content=request.form.get("content")
    edit_title=request.form.get("title")
    edit_author=request.form.get("author")
    created_at=time()
    query('update',DB_TABLE,edit_title,edit_content,edit_author,created_at,pk)
    return redirect('articles/{}'.format(pk))