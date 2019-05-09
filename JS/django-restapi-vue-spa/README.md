# Django API & Vue SPA

## I. 목표

- RESTful API 백엔드 서버 이용
- Vue.js 를 통한 Single Page Application 구축

## II. 과정

## 1. API server

* 지난 프로젝트에 만든 API 서버를 기반으로 발전
* `Score` Model 에 ordering meta class 를 추가해서 최신 평점 순으로 보여 줄 수 있도록 한다.
* `MovieSerializer` 에 `scores` set를 `ScoreSerializer` 통해 보낼 수 있도록 한다.


## 2. Vue

* 페이지 리로드 없이 싱글 페이지에서 돌아가는 SPA 구축

* data

    ```js
    data: {
            genres: [],			// GET 요청으로 받아온 genre
            movies: [],			// GET 요청으로 받아온 movie
            selectedMovie: {},	// Detail 을 보여줄 영화
            selectedGenre: '', 	// 장르별 목록을 보여주기 위한 장르(id)
            check: false, 		// Detail 선택 여부
            scoreInput: '',
            commentInput: '',
            url: "https://insta-shine1225.c9users.io/api/v1/",
        },
    ```

* create

    ```js
    created: function () {
        axios.get(`${this.url}movies/`)
            .then(res => this.movies = res.data);
        axios.get(`${this.url}genres/`)
            .then(res => this.genres = res.data);
    },
    ```

    페이지 로드 시에 가져오는 기본 정보

* methods

    * `selectMovie(movie)`:  상세정보 보여줄 영화를 선택
    * `showList(movie)`:  상세정보에서 나가고, 영화 목록을 보여준다.
    * `scoreSubmit(movie)`:  평점을 등록한다.

* computed, watch

    ```js
    computed: {
        scoreAvg: function () {	// 평균 평점 계산
            let sum = 0
            this.selectedMovie.scores.forEach(score => {
                sum += score.score;
            });
            return sum / this.selectedMovie.scores.length
        }
    },
        watch: {
            selectedGenre: function () { // 필터할 장르 선택, selectbox 에 bind
                this.movies = this.genres[this.selectedGenre - 1].movies
            },
        },
    })
    ```



## 3. View

* 목록과 상세정보 뷰를 `check` 변수에 따라서 동적으로 보여준다.
* 목록에서는 전체 목록 또는 선택된 장르를 보여준다.
* 상세정보에서는 등록된 평점을 볼 수 있으며, 추가로 등록을 할 수 있도록 한다.



