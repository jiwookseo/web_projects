const input = document.querySelector('#js-userinput');
const result = document.querySelector('#result-area');
const tv = document.querySelector('#tv-area');
const btn = document.querySelector('#js-go');
const URL = 'https://api.giphy.com';
const API_KEY = 'aWnhg0AZ0rESAkUIwTFVHhEYFXJWGPUh';
const searchPath = `/v1/gifs/search?api_key=${API_KEY}`;
const giphyAJAXCall = new XMLHttpRequest()
const tvCall = new XMLHttpRequest()

// 1. 인풋 안의 값을 잡는다.
input.addEventListener('keypress', e => {
    if (e.keyCode == 13){
        giphyPush(input.value);
    };
});

btn.addEventListener('click', e => {
    giphyPush(input.value);
});

// 2. GIPHY API 를 통해 data 를 받아서 가공한다.
giphyPush = value => {
    giphyAJAXCall.open('GET', URL + searchPath + '&q=' + value);
    giphyAJAXCall.send();
    giphyAJAXCall.addEventListener('load', e =>{
        const res = e.target.response;
        const json = JSON.parse(res);
        clearToDom(value);
        json.data.forEach(data => pushToDom(data.images.fixed_height.url));
    });
}

// 3. GIF 파일들을 HTML(DOM) 에 밀어넣는다.
const pushToDom = (data) => {
    const gif = document.createElement('img');
    gif.src = data;
    result.appendChild(gif);
    // result.innerHTML += `<img src="${data}"/>`;
};

const clearToDom = (title) => {
    result.innerHTML = `<h2 style="color:white">${title}</h2>`;
};

const onTV = (data) => {
    tv.innerHTML = `<h2 style="color:white">TV</h2><img src="${data}"/>`
};

const tvQuery = ['dog', 'cat', 'samoyed', 'welsh corgi'];
const goTV = tvQuery => {
    tvQuery.forEach(query => {
        tvCall.open('GET', URL + searchPath + '&q=' + query);
        tvCall.send();
        tvCall.addEventListener('load', e =>{
            const tvRes = e.target.response;
            const tvJson = JSON.parse(tvRes);
            onTV(tvJson.data[0].images.fixed_height.url);
            let i = 1;
            window.setInterval(() => {
                data = tvJson.data[i];
                onTV(data.images.fixed_height.url);
                i ++;
            }, 2500);
        });
    });
}
goTV(tvQuery)
