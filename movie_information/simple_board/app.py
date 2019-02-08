from flask import Flask, render_template, request, redirect
import csv
import sqlite3
app=Flask(__name__)
DB_FILE='data/board.splite3'
TABLE='articles'

def query(method, table, *params):
    c=sqlite3.connect(DB_FILE)
    db=c.cursor()
    check=True
    method=method.lower()
    if method=='select_all':
        q='SELECT * FROM {}'.format(table)
    elif method=='select_one':
        q='SELECT * FROM {} WHERE id={}'.format(table,params[0])
    elif method=='create':
        q='INSERT INTO {} (title, content) VALUES ("{}","{}")'.format(table, *params)
    elif method=='update':
        q='UPDATE {} SET title="{}", content="{}" WHERE id="{}"'.format(table, *params)
    elif method=='delete':
        q='DELETE FROM {} WHERE id="{}"'.format(table, *params)
    if method=='select_all' or method=='select_one':
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

@app.route('/')
def index():
    data=query('select_all',TABLE)
    return render_template('index.html',data=data)

@app.route('/submit', methods=["POST"])
def submit():
    title=request.form.get("title")
    content=request.form.get("content")
    query('INSERT',TABLE,title,content)
    return redirect('/')
    
@app.route('/delete',methods=["POST"])
def delete():
    key=request.form.get("id")
    query('DELETE',TABLE,key)
    return redirect('/')

@app.route('/edit',methods=["POST"])
def edit():
    key=request.form.get("id")
    data=query('select_one',TABLE ,key)
    return render_template('edit.html',data=data)

@app.route('/update',methods=["POST"])
def update():
    key=request.form.get("id")
    edit_content=request.form.get("content")
    edit_title=request.form.get("title")
    query('update',TABLE,edit_title,edit_content,key)
    return redirect('/')