from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def main(request):
    return render(request, 'main.html')

def art(request,art_slug):
    if art_slug == "nighthawks":
        data = {
            'title': "Nighthawks",
            'img': "<img src='{% static % 'img/Nighthawks.jpg' %}'>",
            'contents': "Это картина Эдварда хоппера Полуночники"
        }
        return render(request, 'artwork.html', data)
    if art_slug == "mona_lisa":
        data = {
            'title': "Mona lisa",
            'img': "../static/img/monaLisa.png",
            'contents': "Это картина Леонардо Да Винчи Мона Лиза"
        }
        return render(request, 'artwork.html', data)
