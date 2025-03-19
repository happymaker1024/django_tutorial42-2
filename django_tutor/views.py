from django.shortcuts import render
from community.models import Article

def index(request):
    # Article 테이블에서 최근글 3개를 조회
    latest_article_list = Article.objects.all().order_by('-cdate')[:3]
    print(latest_article_list)
    return render(request, 'index.html', {'latest_article_list': latest_article_list})
