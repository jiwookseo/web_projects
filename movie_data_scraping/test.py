from save2csv import save_csv,load_csv
from naverMovie import naverMovie
from kobisMovie import kobisMovie
import os
from pprint import pprint as pp

key = os.getenv('KOBIS_KEY')
client = os.getenv('NAVER_ID')
secret = os.getenv('NAVER_SECRET')

k=kobisMovie(key)
data=k.boxoffice(2019,1,13)
save_csv("boxoffice.csv",data)
data=k.info(data)
save_csv("movie.csv",data)

n=naverMovie(client,secret)
data=n.info(data)
save_csv("movie_naver.csv",data)
n.down_images(data,"images/")