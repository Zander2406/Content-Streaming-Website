from django.shortcuts import render
from django.http import HttpResponse
from django.utils.html import escape
from django.views import View
from .models import *
from django.core.paginator import Paginator


class MainView(View):

    def get(self, request):
        page_data = {'latest_episodes': Episodes.objects.all()[::-1],
                     'popular_ongoing_update': GenreMap.objects.filter(anime__status_id=1).order_by("anime__rating"),
                     'recently_added': Anime.objects.all(),
                     'top_anime': Anime.objects.order_by("rating"),
                     'ongoing': Anime.objects.filter(status_id=1),
                     'genres': Genre.objects.all(),
                     'seasons': Season.objects.all()[::-1],
                     }
        return render(request, 'website/main.html', page_data)


class AnimeView(View):

    def get(self, request, anime_name):
        return render(request, 'website/anime_detail.html')


class WatchView(View):

    def get(self, request, anime_episode):
        return render(request, 'website/play_anime.html')


class GenreView(View):

    def get(self, request, genre):
        return render(request, 'website/play_anime.html')

# Create your views here.
