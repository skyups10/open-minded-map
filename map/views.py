from django.shortcuts import render

def index(request):
    return render(request, 'map/index.html') # 메인 페이지

def seoul(request):
    return render(request, 'map/seoul.html')

def teenager(request):
    return render(request, 'map/teenager.html')