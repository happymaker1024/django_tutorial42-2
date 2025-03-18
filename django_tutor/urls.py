from django.contrib import admin
from django.urls import path
from community.views import write

urlpatterns = [
    path('admin/', admin.site.urls),
    # http://127.0.0.1:8000/write/
    path('write/', write, name='write') # path
]
