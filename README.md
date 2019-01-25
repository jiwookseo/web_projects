# Web project

[source code github repository](https://github.com/jiwookseo/web_project) (private)



## I. 목표

주어진 데이터를 가공해 영화 정보 Web service를 제공한다.

Bootstrap과 CSS를 적절히 사용해 Responsive web page로 제작한다.

+ 추가 목표 :  
  csv file과 Flask를 이용해 동적 web page로 구성한다.



## II. 구성

```bash
$tree
.
|-- README.md
|-- app.py
|-- data.csv
|-- data.xlsx
|-- save2csv.py
|-- static
|   |-- assets
|   |   `-- *.jpg
|   |-- css
|   |   |-- 01_layout.css
|   |   |-- 02_movie.css
|   |   `-- 03_detail_view.css
|   `-- sample
|   |   `-- *.jpg
`-- templates
    |-- 01_layout.html
    |-- 02_movie.html
    |-- 03_detail_view.html
    `-- index.html
```



## III. 과정

### 1. 영화 추천 사이트를 위한 레이아웃 구성  

`templates/1_layout.html` 에 해당한다.

* 상단에는 navigation-bar를 하단에는 copyright와 Go to top of page 버튼 Footer 안에 배치한다.  
  이 때에, 페이지를 스크롤해 움직이더라도 fixed position으로 positioning 해준다.
* viewport와 responsive tier를 사용해서 모든 layout이 디바이스의 너비를 꽉 채우도록한다.

- layout page image

   ![sample image 1](C:/Users/student/web/static/sample/sample_img_0.PNG)



### 2. 영화 추천 사이트를 위한 영화 리스트 구성  

`templates/1_layout.html` 에 해당한다.  

* 손쉬운 Data 사용을 위해 flask app으로 만들어 jinja for문을 이용해 동적으로 제작한다.  

* 영화별 이미지와 장르, 개봉일 등을 출력해주고, 해당하는 네이버 링크로 이동하는 버튼을 제작한다.

* 영화별 평점을 jinja if문을 이용해 9점이상과 미만으로 나누어서 평점 출력 라벨의 색상을 변경해준다.

* 디바이스 크기가 변경되어도 알맞게 출력되도록 responive tier를 이용해 반응형 웹페이지로 제작한다.

* movie age image

  ![sample image 1](C:/Users/student/web/static/sample/sample_img_1.PNG)



### 3. 영화 상세 보기 구현  

```templates/1_layout.html``` 에 해당한다.

- 영화 리스트에서 이미지를 클릭하면 영화의 상세 정보를 보여주는 modal을 제작한다.

- 영화별 고유 코드가 data에 없기 때문에, 해당하는 image 이름을 key로 사용하였다.  
  example modal ID :  `#movie-{{ item['images'] }}-modal`

- 상세 정보에는 해당하는 영화의 img를 carousel로 슬라이드 해줄 수 있도록 한다.

- detail_view page image  ~~메라 짱짱~~ 

  ![sample image 1](C:/Users/student/web/static/sample/sample_img_2.PNG)