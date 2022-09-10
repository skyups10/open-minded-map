from django.shortcuts import render
import requests
from bs4 import BeautifulSoup

# Create your views here.
def index(request):
    url = 'https://search.naver.com/search.naver?where=news&ie=utf8&sm=nws_hty&query=%EC%A0%95%EC%8B%A0%EA%B1%B4%EA%B0%95'
    req = requests.get(url)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')

    title = [title['title'] for title in soup.find_all('a', attrs={'class':'news_tit'})]
    url = [ url['href'] for url in soup.find_all('a', attrs={'class':'news_tit'}) ]
    context = {'title':title, 'url':url}
    return render(request,'news/news.html', context)