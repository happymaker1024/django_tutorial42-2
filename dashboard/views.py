from django.shortcuts import render

# Create your views here.
def dashboard(request):
    # 비즈니스 로직
    
    return render(request, 'dashboard.html', )