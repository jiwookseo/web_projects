import os
import csv
import requests
from datetime import datetime, timedelta

kobis_key = os.getenv('KOBIS_KEY')
kobis_info_url="http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json"
kobis_boxoffice_url="http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json"

class kobisMovie:
    def __init__(self,key):
        self.key=key
        self.info_url="http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json"
        self.boxoffice_url="http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json"
    
    def boxoffice(self,year,month,day):
        # kobisMovie.boxoffice(2019,1,13)
        dt=datetime(year,month,day)
        td=timedelta(days=7)
        targets=[dt]
        for _ in range(9):
            dt-=td
            targets.append(dt)
        targets=[temp.strftime("%Y%m%d") for temp in targets]
        result={}
        for target in targets[::-1]:
            params={"key":self.key,"targetDt":target,"weekGb":"0"}
            doc=requests.get(self.boxoffice_url,params=params).json()
            for l in doc["boxOfficeResult"]["weeklyBoxOfficeList"]:
                result[l["movieCd"]]=(l["movieNm"],l["audiAcc"],target)
        return [[k,*v] for k,v in result.items()]
    
    def info(self,data):
        # data=kobisMovie.boxoffice(year,month,day)
        result=[]
        for item in data:
            params={"key":kobis_key,"movieCd":item[0]}
            doc=requests.get(kobis_info_url,params=params).json()
            info=doc["movieInfoResult"]["movieInfo"]
            temp=[]
            temp.append(item[0])
            temp.append(info["movieNm"])
            temp.append(info["movieNmEn"])
            temp.append(info["movieNmOg"])
            temp.append(info["prdtYear"])
            temp.append(info["showTm"])
            temp.append("/".join([temp["genreNm"] for temp in info["genres"]]))
            temp.append(info["directors"][0]["peopleNm"])
            temp.append(info["audits"][0]["watchGradeNm"])
            for _ in range(min(len(info["actors"]),3)):    
                temp.append(info["actors"].pop(0)["peopleNm"])
            result.append(temp)
        return result