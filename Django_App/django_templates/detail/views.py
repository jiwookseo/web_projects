from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')
    
def qna(request):
    return render(request,'qna.html')
    
def mypage(request):
    a={'title':'보노보노','content':'ぼのぼの. 보노보노의 주인공. 종족은 해달. 사는 곳은 바다가 있는 절벽가.','image':'https://s3.namuwikiusercontent.com/s/3f3287de7897b315855354f535b48f97d3e016603240148cb1768aedfc23010324f794e3ecd14da764960544e4d0d0859ce850117e5ea81e4dd0a9264f03db6da803483c0bf195d7e7607f9437046392fbdf4f32f79ded12d2dbeebadd4ff493','url':'https://namu.wiki/w/%EB%B3%B4%EB%85%B8%EB%B3%B4%EB%85%B8(%EB%B3%B4%EB%85%B8%EB%B3%B4%EB%85%B8)'}
    b={'title':'포로리','content':'シマリスくん. 보노보노의 친구. 일본 이름은 시마리스 군, 즉 다람쥐 군이다(...). 이름대로 종족은 다람쥐.','image':'https://s3.namuwikiusercontent.com/s/e1c088d19b02520e246b0b48e1d5ed849f1fcadbd505994cc5b05479757f9fa1a0d90fb72b65312c91b325313fa1f4ba9d76f0379320d8119b253226738a2b52ade619c8ae75c5bcbccd9766d343655df577b78f46fba5bf3a90ce1e25e57f01','url':'https://namu.wiki/w/%ED%8F%AC%EB%A1%9C%EB%A6%AC'}
    c={'title':'너부리','content':'アライグマくん. 보노보노의 등장인물. 성격은 도라에몽에 등장하는 퉁퉁이와 똑같다고 보면 된다.','image':'https://s3.namuwikiusercontent.com/s/a9335336ae85efe98d27b0e32de10c61917cc77e70316f008f3abdd38238c02f738392a67ea2d5383887bafdcbddc16b1f492bd9feeb316fbdb580c1cf2eef4b6b8351c2bca9adfd110d20532818f7112c8b13f416bb1e26efd6b651a03805dd','url':'https://namu.wiki/w/%EB%84%88%EB%B6%80%EB%A6%AC'}
    articles=[a,b,c]
    return render(request,'mypage.html',{'articles':articles})
    
def signup(request):
    return render(request,'signup.html')
    
def notfound(request,not_found):
    return render(request,'notfound.html',{'not_found':not_found})