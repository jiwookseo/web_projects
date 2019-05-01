const API_KEY = "" // api key required
const URL = `https://api.themoviedb.org/3/movie/popular?api_key=${API_KEY}`
const imgURL = 'http://image.tmdb.org/t/p/w200'

// 1. 빈 무비 데이터를 가지고 있는 Vue 인스턴스가 만들어진다.
// 2. completed 함수가 실행되면서 movies 를 불러온다.
// 3. 불러온 movies 를 vue 의 data 안의 movies 에 할당한다.

const app = new Vue({
    el: '#main',
    data: {
        searchString: "",
        movies: NaN
    },
    computed: {
        filteredMovies: function () {
            if (!this.searchString) {
                return this.movies
            };
            let searchString = this.searchString.trim().toLowerCase();
            return this.movies.filter(movie => movie.title.toLowerCase().includes(searchString))  // 키워드가 포함 되어있는 지 필터
        }
    },
    async created() {  // vue 인스턴스가 초기화 되고나서 실행하는 함수
        const response = await axios.get(URL);
        this.movies = response.data.results.map(movie => {
            movie.poster_path = imgURL + movie.poster_path  // poster_path = "/or06FN3Dka5tukK1e9sl16pB3iy.jpg"
            return movie
        });
    }
})
