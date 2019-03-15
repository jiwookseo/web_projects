# Django DB design Project

## I. 목표

* 데이터를 생성, 조회, 삭제, 수정할 수 있는 Web Application 제작
* 데이터베이스 테이블간 관계 설정(1:N)



## II. 구성

### 1. Tree

```bash
$ tree -d
.
|-- movies
|   |-- migrations
|   `-- templates
|       `-- movies
|-- project_07_db
`-- templates
```



### 2. DB model

`Genre`,` Movie`, `Score` 순으로 각각 1:N 관계를 갖는다.



### 3. Templates

* `base.html`  

  레이아웃 html

* `list.html`

  전체 Movie를 보여주는 template

*  `detail.html` 

  `movie_id`를 받아 동적으로 해당하는 Movie의 정보, 유저평가를 보여주는 template

*  `update.html`

  `movie_id `를 받아 동적으로 해당하는 Movie의 정보를 수정할 수 있는 template



## III. 과정

### 1. Model

```python
class Genre(models.Model):
    name = models.CharField(max_length=20, default='')
# Genre model

class Movie(models.Model):
    title = models.CharField(max_length=30, default='')
    audience = models.IntegerField(default=0)
    poster_url = models.CharField(max_length=140, default='')
    description = models.TextField(default='')
    genre = models.ForeignKey(Genre, on_delete=models.PROTECT, default=None)
# Genre object를 ForeignKey로 받는 Movie model

class Score(models.Model):
    content = models.CharField(max_length=140, default='')
    score = models.IntegerField(default=0)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, default=None)
# Movie object를 ForeignKey로 받는 Score model
```

* 앞서 말한 내용처럼 `Genre` - `Movie` - `Score` 로 이어지는 1:N, 1:N 관계모델



### 2. Urls

```python
path('', views.movie_list, name="movie_list"),
path('<int:movie_id>/', views.movie_detail, name="movie_detail"),
path('<int:movie_id>/update/', views.movie_update, name="movie_update"),
path('<int:movie_id>/delete/', views.movie_delete, name="movie_delete"),
path('<int:movie_id>/scores/new', views.score_new, name="score_new"),
path('<int:movie_id>/scores/<int:score_id>/delete', views.score_delete, name="score_delete"),
```

* index에서는 list template를 보여준다.

* update 같은 경우에는 GET method는 수정 template, POST method는 객체 업데이트를 실행
* score같은 경우에는 `movie_id`와 `score_id`를 모두 관리해야한다.



### 3. Views

```python
def movie_delete(request, movie_id):
    if request.method == 'POST':
        
def movie_update(request, movie_id):
    if request.method == 'POST':
        
def score_new(request, movie_id):
    if request.method == 'POST':
        
def score_delete(request, movie_id, score_id):
    if request.method == 'POST':
```

* DB를 변경하는 위 코드들은 반드시 method가 POST인 경우에만 실행한다.

  

```python
def movie_update(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    if request.method == 'POST':
		# ......
    else:
        return render(request, 'movies/update.html', {'movie': movie, 'genres': Genre.objects.all()})
```

* 특별히 movie_update의 GET 요청에서는 `Genre.objects.all()` 을 인자로 넘겨준다.

  업데이트 Template에서 해당하는 Genre set을 select box로 사용하기 위함



### 4. Templates

* `detail.html`

    ```python
    <p class="card-text">{{ movie.description|linebreaks }}</p>
    ```

    * `description` Field는 여러 줄의 문자를 담고 있는 `TextField` 이므로

      `|linebreaks` 필터를 이용해 개행처리



* `update.html`

    ```html
    <textarea class="form-control" id="description" name="description" rows="3"
    >{% for foo in movie.description.splitlines %}{{ foo }}
    {% endfor %}</textarea>
    <!-- splitlines를 이용한 textarea 개행처리 -->
    ```

    * `TextField`인  `description`은 `<textarea>` 를 이용해 출력했다.

    * `|linebreaks` 필터를 이용한 방식은 `<p>` 와 `<br>` 를 이용한 방식이므로 tag 까지 그대로 출력하게 된다. 

      따라서 `splitlines method`와 `Enter`입력으로 개행할 수 있도록 처리

    

    ```html
    <select class="form-control" id="genre" name="genre">
        {% for gerne in gernes %}
        {% if gerne.id == movie.genre_id %}
        <option value="{{ gerne.id }}" selected>{{ gerne.name }}</option>
        {% else %}
        <option value="{{ gerne.id }}">{{ gerne.name }}</option>
        {% endif %}
        {% endfor %}
    </select>
    <!-- for syntax 이용한 genre select box, if syntax 이용해 selected 처리 -->
    ```

    * `Genre` 선택을 위한 select box
    * 인자로 받은 `Genre.objects.all()` 을 이용한다.
    * 현재 `Movie.genre_id` 와 `forloop`의 `genre.id`를 비교해 `selected` 처리해 기본값을 설정

