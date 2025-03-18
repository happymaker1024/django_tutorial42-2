from django.shortcuts import render
from .forms import Form

# Create your views here.
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
    else:
        form = Form()  # Form() 객체 생성
    # return render(request, 'write.html', {'키':파이썬변수})
    return render(request, 'write.html', 
                  {'hello_django':hello, 'form':form})