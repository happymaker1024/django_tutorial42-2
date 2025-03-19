from django.shortcuts import redirect, render
from django.urls import reverse

from .models import Article
from .forms import Form

# Create your views here.

def articleList(request):
    # Article클래와 연결된 테이블의 모든 레코드를 조회
    article_list = Article.objects.all()
    # print(article_list)
    # for a in article_list:
    #     print("이름: ", a.name, "제목: ", a.title)
    return render(request, 'list.html', {'article_list': article_list})

def write(request):
    # 비즈니스 로직 구현
    hello = "안녕 장고"
    # 사용자 요청 method POST일때
    if request.method == 'POST':
        # request.POST 데이터를 폼객로 생성
        form = Form(request.POST)
        # print(form)
        # form 데이터 유효성 검증
        if form.is_valid():
            # DB 테이블에 저장
            form.save()
            return redirect(reverse('community:list'))
    else:
        form = Form()  # Form() 객체 생성
    # return render(request, 'write.html', {'키':파이썬변수})
    return render(request, 'write.html', 
                  {'hello_django':hello, 'form':form})


def viewDetail(request, num=1):
    article_detail = Article.objects.get(id=num)
    print("article_detail : ", article_detail)
    return render(request, 'view_detail.html', {'article_detail':article_detail})