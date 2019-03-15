from flask import Flask, render_template, request
import csv, json
import requests
import os
from pprint import pprint as pp
app=Flask(__name__)

riot_key="api_key={}".format(os.getenv("RIOT_KEY"))

@app.route('/')
def index():
    return render_template("index.html")

methods={}

def getApi(kind, method, params):
    url = "https://kr.api.riotgames.com/lol/{}/v4/{}/{}".format(kind,method,params)
    #print("get to api {}".format(url))
    return requests.get(url).json()

# j=requests.get("http://ddragon.leagueoflegends.com/cdn/6.24.1/data/en_US/champion.json").json()
# champ=j["data"]
# champ_byid={}
# for data in champ.values():
#     champ_byid[data["key"]]=[data["id"]]
#     champ_byid[data["key"]].append("http://ddragon.leagueoflegends.com/cdn/6.24.1/img/champion/{}.png".format(data["id"]))
# pp(champ_byid)
# with open("champ.json","w") as f:
#     json.dump(champ_byid,f)


@app.route('/summoner', methods=["GET"])
def summoner():
    user_name=request.args.get("user_name")
    
    res=getApi("summoner","summoners/by-name","{}?{}".format(user_name,riot_key))
    pp(res)
    user_id=res["id"]
    user_accountId=res["accountId"]
    user_name=res["name"]
    user_level=res["summonerLevel"]
    
    res=getApi("league","positions/by-summoner","{}?{}".format(user_id,riot_key))
    queue={}
    for i in res:
        if i["queueType"]=="RANKED_SOLO_5x5":
            queueType="5:5 솔로 랭크"
        elif i["queueType"]=="RANKED_FLEX_SR":
            queueType="5:5 자유 랭크"
        else:
            queueType="3:3 자유 랭크"
        wins=i["wins"]
        losses=i["losses"]
        tier=i["tier"]
        leaguePoints=i["leaguePoints"]
        rank=i["rank"]
        queue[queueType]={"wins":wins,"losses":losses,"rank":rank,"leaguePoints":leaguePoints,"tier":tier}
    # pp(queue)
    ends=9
    begins=0
    end="endIndex={}".format(ends)
    begin="beginIndex={}".format(begins)
    res=getApi("match","matchlists/by-account","{}?{}&{}&{}".format(user_accountId,end,begin,riot_key))
    # pp(res)
    matches=res["matches"]
    matchdata=[]
    for match in matches:
        res=getApi("match","matches","{}?{}".format(match["gameId"],riot_key))
        for participant in res["participantIdentities"]:
            if participant["player"]["accountId"]==user_accountId:
                participantId=participant["participantId"]
                break
        dd={}
        data=res["participants"][participantId-1]
        for i in ["win","kills","deaths","assists"]:
            dd[i]=data["stats"][i]
        for i in ["championId","spell1Id","spell2Id"]:
            dd[i]=str(data[i])
        dd["posi"]=data["timeline"]["lane"]+" lane / "+data["timeline"]["role"]
        matchdata.append(dd)
    with open('champ.json', 'r') as f:
        champ = json.load(f)
    # pp(matchdata)
    return render_template("summoner.html",user_name=user_name,user_level=user_level,queue=queue,matchdata=matchdata,champ=champ)