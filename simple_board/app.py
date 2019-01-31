from flask import Flask, render_template, request
import csv
import sqlite3
app=Flask(__name__)

@app.route('/')
def index():
    c=sqlite3.connect('data/board.splite3')
    db=c.cursor()
    query='SELECT * FROM articles'
    db.execute(query)
    data=db.fetchall()
    c.close()
    return render_template('index.html',data=data)

@app.route('/create', methods=["POST"])
def create():
    title=request.form.get("title")
    content=request.form.get("content")
    c=sqlite3.connect('data/board.splite3')
    db=c.cursor()
    query='INSERT INTO articles (title, content) VALUES ("{}","{}")'.format(title, content)
    db.execute(query)
    c.commit()
    c.close()
    return render_template('create.html')
    
@app.route('/delete',methods=["GET"])
def delete():
    key=request.args.get("id")
    c=sqlite3.connect('data/board.splite3')
    db=c.cursor()
    query='DELETE FROM articles WHERE id="{}"'.format(key)
    db.execute(query)
    c.commit()
    c.close()
    return render_template('delete.html')

@app.route('/edit',methods=["GET"])
def edit():
    key=request.args.get("id")
    c=sqlite3.connect('data/board.splite3')
    db=c.cursor()
    query='SELECT * FROM articles WHERE id="{}"'.format(key)
    db.execute(query)
    data=db.fetchall()
    c.close()
    return render_template('edit.html',data=data)

@app.route('/update',methods=["POST"])
def update():
    key=request.form.get("id")
    edit_content=request.form.get("content")
    edit_title=request.form.get("title")
    c=sqlite3.connect('data/board.splite3')
    db=c.cursor()
    query='UPDATE articles SET title="{}", content="{}" WHERE id="{}"'.format(edit_title,edit_content,key)
    db.execute(query)
    c.commit()
    c.close()
    return render_template('update.html')
