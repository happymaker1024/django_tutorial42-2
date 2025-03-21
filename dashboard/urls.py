from django.urls import path

from dashboard.views import dashboard

app_name = "dashboard"  
urlpatterns = [
    # http://127.0.0.1:8000/dashboard/
    path('dashboard/', dashboard, name='dashboard'), # path
]
