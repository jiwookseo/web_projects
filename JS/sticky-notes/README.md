# Stick Notes

## Django Rest Framework

1. Django rest framework 로 api 서버를 만든다
2. `content` 필드 1개를 가지고 있는 `Memo` 모델을 만든다.
3. POST 요청으로 Memo 를 create 할 수 있다.
   - POST http://localhost:8000/api/v1/memos/
4. GET 요청으로 모든 Memo 를 read 할 수 있다.
   - GET http://localhost:8000/api/v1/memos/

## Vue.js

1. textarea 태그와 Vue 의 data 인 `content` 를 양방향 바인딩한다.
2. `created` life cycle 에서 axios 로 위 api 서버에서 memos 를 불러온 뒤 Vue 의 data 인 memos 에 바인딩한다.
3. submit 버튼이 눌리면 axios 로 위 api 서버로 `content` 의 내용을 작성한뒤 응답받은 memo 를 Vue 의 memos 에 push 한다.
4. memo 가 작성될때마다 textarea 의 값은 초기화된다.

