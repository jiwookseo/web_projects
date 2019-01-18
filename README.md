# Fake watcha service

영화진흥위원회 오픈 API와 네이버 영화 검색 API를 이용한 fake-watcha, 영화평점사이트

[source code github repository](https://github.com/jiwookseo/fake_watcha) (private)



## I. 데이터 수집

### 영화진흥위원회 오픈 API

영화진흥위원회 API는 api key 정보 headers를 가진 GET requests를 통해 데이터를 받아온다.

* 주간/주말 박스오피스 데이터 API

   1. parameter로 날짜 정보를 받아서 해당 날짜까지 10주간 주간 데이터를 받아온다.

   2. 데이터에서 필요한 고유코드, 영화제목, 누적관람객수 등을 가공해 list로 리턴해준다.

   3. source code

      ```python
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
      ```

* 영화 상세정보 API

   1. 위에서 가져온 박스 오피스 데이터, 그 중 movieCd, 고유코드를 이용해 영화별 상세정보를 받아온다.

   2. 받아온 데이터 중 필요한 정보를 가공해서 list로 반환해준다.
      예외사항이 발생할 수 있는 배우 항목은 min, len을 이용해 횟수를 제한하여서 받아온다.

   3. source code

      ```python
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
      ```



### 네이버 검색 API

* 네이버 영화 검색 API
  1. 앞서 영화진흥위원회 API를 통해 가져온 영화이름 데이터를 이용해 영화 정보를 받아온다.
  2. 네이버는