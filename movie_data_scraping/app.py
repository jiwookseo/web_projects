from flask import Flask,request,render_template
from save2csv import save_csv,load_csv

app=Flask("__name__")

office_data=load_csv("boxoffice.csv")
office_dict={x[0]:x[1:] for x in office_data}
movie_data=load_csv("movie.csv")
movie_dict={x[0]:x[1:] for x in movie_data}
naver_data=load_csv("movie_naver.csv")
naver_dict={x[0]:x[1:] for x in naver_data}
nametocode={x[1]:x[0] for x in office_data}


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/search',methods=["GET"])
def search():
    q=request.args.get("q")
    movie_code=nametocode[q]
    return render_template("search.html",q=q,office=office_dict[movie_code],naver=naver_dict[movie_code],movie=movie_dict[movie_code])
    
@app.route('/boxoffice')
def boxoffice():
    movie_code=[x[0] for x in office_data if x[-1]=='20190113']
    return render_template("boxoffice.html",cd=movie_code,office=office_dict,naver=naver_dict,movie=movie_dict)