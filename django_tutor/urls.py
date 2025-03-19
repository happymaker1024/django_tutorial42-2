from django.contrib import admin
from django.urls import include, path
from django_tutor.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    # http://127.0.0.1:8000/
    path('', index, name='index'),

    # http://127.0.0.1:8000/write/
    # http://127.0.0.1:8000/list/
    # http://127.0.0.1:8000/view_detail/
    path('', include('community.urls')),    
]
