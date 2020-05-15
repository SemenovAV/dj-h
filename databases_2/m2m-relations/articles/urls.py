from articles.views import articles_list
from django.urls import path

urlpatterns = [
    path('', articles_list, name='articles'),
]
