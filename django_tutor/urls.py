from django.contrib import admin
from django.urls import path
from community.views import articleList, index, viewDetail, write

urlpatterns = [
    path('admin/', admin.site.urls),
    # http://127.0.0.1:8000/write/
    path('write/', write, name='write'), # path
    path('list/', articleList, name='list'),
    # http://127.0.0.1:8000/view_detail/1
    path('view_detail/<int:num>/', viewDetail, name='detail'),
    # http://127.0.0.1:8000/
    path('', index, name='index'),
    
]
