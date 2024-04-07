from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def main(request):
    return render(request, 'main.html')


def art(request,art_slug):
    if art_slug == "nighthawks":
        data = {'title': "Nighthawks",
                'contents': "Это картина Эдварда хоппера Полуночники",
                'price': "800$",
                'list': ["Самый большой аукцион в мире", "Качественная продукция", "Более 9000 произведений искусства"]}
        return render(request, 'artwork.html', data)
    if art_slug == "mona_lisa":
        data = {'title': "Mona lisa",
                'contents': "Это картина Леонардо Да Винчи Мона Лиза",
                'price': "1200$",
                'list': ["Самый большой аукцион в мире", "Качественная продукция", "Более 9000 произведений искусства"]}
        return render(request, 'artwork.html', data)
