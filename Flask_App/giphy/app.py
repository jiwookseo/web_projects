from flask import Flask, request, render_template
import os
import requests
from pprint import pprint as pp
app=Flask(__name__)
api_key=os.getenv("API_KEY")

def q2j(method,limit=16):
    url="http://api.giphy.com/{}api_key={}&limit={}".format(method,api_key,limit)
    print(url)
    return requests.get(url).json()

def j2gl(j):
    return [(data["images"]["original"]["url"],data["slug"],data["bitly_url"]) for data in j.get("data")]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search", methods=["GET"])
def search():
    q=request.args.get("q")
    j=q2j("v1/gifs/search?q={}&".format(q),20)
    total=j["pagination"]["total_count"]
    gifs=j2gl(j)
    return render_template("search.html",q=q,gifs=gifs,total=total)
    
@app.route("/trending")
def trending():
    limit=16
    j=q2j("v1/stickers/trending?",limit)
    gifs=j2gl(j)
    total=j["pagination"]["total_count"]
    return render_template("trending.html",gifs=gifs,limit=limit,total=total)

# @app.route("/block")
# def block():
#     return render_template("block.html")