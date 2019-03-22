# Django DB Seeding Project

## I. 목표

- Seed Data를 활용한 DB 설계
- Django ModelForm을 통한 validation 및 Create, Update
- 유사한 코드를 최소화



## II. 구성

### 1. Tree

```bash
$ tree -d
.
|-- movies
|   |-- migrations
|   |-- fixtures
|   `-- templates
|       `-- movies
|-- project_07_db
`-- templates
```



### 2. Forms

* `Movie` Model을 위한 `MovieModelForm` 작성

* `Score` Model을 위한 `ScoreModelForm` 작성



### 3. Views

- `base.html`  

  레이아웃 html

- `list.html`

  전체 Movie를 보여주는 template

- `detail.html` 

  `movie_id`를 받아 동적으로 해당하는 Movie의 정보, 유저평가를 보여주는 template

- `update.html`

  `movie_id `를 받아 동적으로 해당하는 Movie의 정보를 수정할 수 있는 template



## III. 과정

### 0. Seed data load

* `movies/fixtures` directory에 있는 seed data를 로드해준다.

  ```bash
  $ python manage.py loaddata genre.json
  $ python manage.py loaddata movie.json
  ```



### 1. Forms

* `MovieModelForm`

    ```python
    class MovieModelForm(forms.ModelForm):
        class Meta:
            model = Movie
            fields = ['title', 'audience', 'poster_url', 'description', 'genre']
            widgets = {
                'title': forms.TextInput(
                    attrs={
                        'class': 'form-control',
                        'placeholder': 'Enter Title'
                    }
                ),
                'audience': forms.NumberInput(
                    attrs={
                        'class': 'form-control',
                        'placeholder': 'Enter Audience'
                    }
                ),
                'poster_url': forms.URLInput(
                    attrs={
                        'class': 'form-control',
                        'placeholder': 'Enter Poster URL'
                    }
                ),
                'description': forms.Textarea(
                    attrs={
                        'class': 'form-control',
                        'rows': 7,
                        'placeholder': 'Enter Description'
                    }
                ),
                'genre': forms.Select(
                    attrs={
                        'class': 'form-control',
                        'placeholder': 'Select Genre'
                    }
                ),
            }
    ```

    * Bootstrap 클래스를 적용시키기 위해 widgets에 attributes를 추가해주었다.

    * `Genre` ForeignKey는 Select box를 이용하고,

      `Genre` Model에 `__str__ ` function을 overwrite 해서 `self.name` 을 return하여 사용자가 쉽게 `Genre` 선택할 수 있도록 했다.

    

* `ScoreModelForm`

    ```python
    class ScoreModelForm(forms.ModelForm):
        class Meta:
            model = Score
            fields = ['score', 'content', 'movie']
            widgets = {
                'score': forms.NumberInput(
                    attrs={
                        'class': 'form-control my-1',
                        'placeholder': 'Score',
                        'min': 0,
                        'max': 10,
                        'step': 1
                    }
                ),
                'content': forms.TextInput(
                    attrs={
                        'class': 'form-control my-1',
                        'placeholder': 'Content',
                        'style': 'width: 280px'
                    }
                ),
                'movie': forms.HiddenInput()
            }
    ```

    * `MovieModelForm` 과 동(同), Bootstrap 클래스를 적용시키기 위해 widgets에 attributes를 추가해주었다.
    * `Movie` ForeignKey는 따로 입력받는 변수가 아니므로 `HiddenInput`을 사용한다.

### 2. Views
* `views.movie_new`

    New form 과 create를 담당한다.

    ```python
    def movie_new(request):
        if request.method == 'POST':
            form = MovieModelForm(data=request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Successfully registered')
                return redirect('movies:movie_detail', form.id)
            else:
                messages.success(request, 'Failed to register, check your input')
        else:
            form = MovieModelForm()
        return render(request, 'movies/form.html', {'form': form})
    ```

    * `Method:GET` : form.html 을 render

    * `Method:POST` : POST로 받은 데이터의 validation에 따라 message를 출력해준다.

      만약 성공이라면 해당 영화의 디테일 페이지를 redirect

      실패라면 입력된 데이터를 유지한채로 form.html을 render해준다.

      * 이때 실패하는 경우는, 사용자가 악의적으로 form을 변경하는 등의 isuue

      

* `views.movie_update`

    Edit form과 update를 담당한다.

    ```python
    def movie_update(request, movie_id):
        movie = Movie.objects.get(id=movie_id)
        if request.method == 'POST':
            form = MovieModelForm(instance=movie, data=request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Successfully updated')
                return redirect('movies:movie_detail', movie.id)
            else:
                messages.success(request, 'Failed to update, check your input')
        else:
            form = MovieModelForm(instance=movie)
        return render(request, 'movies/form.html', {'form': form})
    ```

    - `Method:GET` : `instance`로 해당하는 `Movie`를 가진  form.html 을 render

    - `Method:POST` : `views.movie_new`와 동(同)

      

* `views.movie_detail`

    영화 디테일 페이지, 영화 상세정보와 1:N 관계로 등록된 `Score`를 출력해준다.

    `Method:POST`를 통해 `Score` create도 겸한다.

    ```python
    def movie_detail(request, movie_id):
        movie = Movie.objects.get(id=movie_id)
        if request.method == 'POST':
            form = ScoreModelForm(data=request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Successfully scored')
            else:
                messages.success(request, 'Failed to score, check your input')
                return render(request, 'movies/detail.html', {'movie': movie, 'form': form})
        form = ScoreModelForm(initial={'movie': movie})
        return render(request, 'movies/detail.html', {'movie': movie, 'form': form})
    ```

    - `Method:GET` : `instance`로 해당하는 `Movie`를 가진  form.html 을 render

    - `Method:POST` : `views.movie_new`, `views.movie_update`와 유사하지만,

      앞서 말한 것 같이 ForeignKey로 `movie`를 가지고 있지만 입력을 받지 않는 HiddenInput이므로

      form을 생성 할 때에 initial 인자로 `{'movie': movie}`를 넘겨주어 hidden value를 지정해준다.

      

### 3. Templates

* `base.html`

    ```html
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
        <a class="navbar-brand" href="{% url 'movies:movie_list' %}">WookCha</a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent"
                aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
            <ul class="navbar-nav ml-auto">
                <!-- loginout -->
                <li class="nav-item">
                    <a class="nav-link" href="{% url 'movies:movie_new' %}">New-Movie</a>
                </li>
            </ul>
        </div>
    </nav>
    ```

    편리함을 위해 Navbar 단을 추가

    ```html
    {% if messages %}
        {% for message in messages %}
            <div class="alert alert-info alert-dismissible fade show" role="alert">
                {{ message }}
                <button type="button" class="close" data-dismiss="alert" aria-label="Close">
                    <span aria-hidden="true">&times;</span>
                </button>
            </div>
        {% endfor %}
    {% endif %}
    ```

    Navbar 하단에 Success, Fail Message를 출력할 수 있는 Alert 단 생성

* `form.html`

    ```html
    {% extends 'movies/base.html' %}
    {% block title %}
        {% if form.instance.id %}
            Update Movie
        {% else %}
            New Movie
        {% endif %}
    {% endblock %}
    ```

    New 와 Update로 모두 사용되므로, instance가 실제로 존재하는 `Movie`인지 분기를 나누어 Title을 출력한다.

    ```html
    <!-- movie form part -->
    <form method="POST" class="mt-5">
        {% csrf_token %}
        {{ form.as_p }}
        <input type="submit" class="btn btn-outline-dark d-flex ml-auto" value="submit">
    </form>
    ```

    `form.as_p`를 사용해 form을 생성한다.

* `detail.html`

    ```html
    <!-- score form part -->
    <div class="card-body">
        <form action="" method="POST"
              class="form-row d-flex justify-content-between px-2">
            {% csrf_token %}
            {% for field in form %}
            <div class="from-group">
                {{ field }}
            </div>
            {% endfor %}
            <div class="from-group">
                <input type="submit" id="submit" value="submit"
                       class="form-control btn btn-outline-dark my-1">
            </div>
        </form>
    </div>
    ```

    score form은 form-row로 사용하기 위해서 field 단위로 for문을 돌려서 from-group으로 둘러싸주었다.
