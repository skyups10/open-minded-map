from django.shortcuts import render

def index(request):
    return render(request, 'map/index.html') # 메인 페이지