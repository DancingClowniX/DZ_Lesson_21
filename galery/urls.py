from django.urls import path, re_path
import galery.views as galery

urlpatterns = [
    path('', galery.main, name='main_url'),
    path('<slug:art_slug>/', galery.art),
]