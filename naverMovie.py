import os
import requests
import shutil
import time
from bs4 import BeautifulSoup as bs

class naverMovie:
    def __init__(self,client,secret):
        self.headers={"X-Naver-Client-Id":client,"X-Naver-Client-Secret":secret}
        self.info_url=f"https://openapi.naver.com/v1/search/movie.json"
    
    def info(self,data):
        # data=[[movieCd,movieNm,...],[..],...] ->> kobisMovie.info()
        result=[]
        for item in data:
            params={"query":item[1]}
            doc=requests.get(self.info_url,params=params,headers=self.headers).json()
            
            link=doc["items"][0]["link"]
            naverCode=link[link.find("=")+1:]
            origin_image=f"https://movie.naver.com/movie/bi/mi/photoViewPopup.nhn?movieCode={naverCode}" # 원본 사이즈 이미지 팝업 url
            res=requests.get(origin_image).text
            doc2 = bs(res, 'html.parser')
            res=doc2.find("img")
            origin_url = res.get("src") # 이 url이 원본 사이즈 이미지

            result.append([item[0],doc["items"][0]["image"],link,doc["items"][0]["userRating"],origin_url])
            time.sleep(0.05)
        return result
    
    def down_images(self,data,images_dir):
        # data=naverMovie.info()
        # images_dir="images/"
        # scraping 한 이미지가 110*158 으로 사용하기에 너무 작다. -> 원본 이미지 스크래핑 해서 사용
        for item in data:
            getImage(item[1],f"{images_dir}{item[0]}_thumb.jpg") # 썸네일 사이즈 이미지
            getImage(item[4],f"{images_dir}{item[0]}_origin.jpg") # 원본 사이즈 이미지
        return None

def getImage(url,imgDir):
    response = requests.get(url, stream=True)
    with open(imgDir, 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)
