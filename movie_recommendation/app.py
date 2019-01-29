from flask import Flask, request, render_template
from save2csv import load_csv
from pprint import pprint as pp
app=Flask(__name__)

# data load
raw=load_csv("data.csv")

# data convert
data=[]
col="movieNm	movieNmEn	audiAcc	openDt	GenreNm	watchGradeNm	Naver	Score	Description".split()
for i in raw:
    d={}
    for index in range(len(i)):
        d[col[index]]=i[index]
    data.append(d)
for i in data:
    i["Score"]=float(i["Score"])
    i["Score"]=float(i["Score"])
    i["openDt"]=i["openDt"][:4]+"."+i["openDt"][4:6]+"."+i["openDt"][6:8]
    result=""
    count=0
    for temp in i["audiAcc"][::-1]:
        result+=temp if count%3!=0 or count==0 else ","+temp
        count+=1
    i["audiAcc"]=result[::-1]
    i["Description"]=i["Description"].split("\n")
data[3]["movieNm"]="주먹왕 랄프2"
images="20176251 20180290 20182544 20184105 20186324 20189463".split()
order=[1,5,2,0,4,3]
for i in order:
    data[i]["images"]=images.pop(0)
    data[i]["thumb"]="assets/"+data[i]["images"]+".jpg"
    data[i]["imgs"]=[]
    for j in range(1,4):
        data[i]["imgs"].append("assets/"+data[i]["images"]+"-"+str(j)+".jpg")

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/layout')
def layout():
    return render_template("01_layout.html")

@app.route('/movie')
def movie():
    return render_template("02_movie.html",movies=data)

@app.route('/detail_view')
def detail_view():
    return render_template("03_detail_view.html",movies=data)