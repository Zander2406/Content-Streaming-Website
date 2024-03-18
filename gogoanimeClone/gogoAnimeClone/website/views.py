from django.shortcuts import render
from django.http import HttpResponse
from django.utils.html import escape
from django.views import View
from .models import *


class MainView(View):

    def get(self, request):
        main_anime = {'name': 'Solo Leveling', 'episode': 6}
        popular_anime = {'name': 'Solo Leveling', 'genres': ['Action', 'Shounen', 'Adult'], 'latest_episode': 6}
        anime_name = 'Solo Leveling'
        top_anime = {'name': 'Solo Leveling', 'episode': 6}
        ongoing = 'Solo Leveling'
        genre = 'Adventure'
        page_data = {'summary': 'This is a summary',
                     'latest_episodes': Episodes.objects.all()[::-1],
                     'popular_anime': Anime.objects.order_by("rating"),
                     'recently_added': Anime.objects.all(),
                     'top_anime': Anime.objects.order_by("rating"),
                     'ongoing': Anime.objects.filter(status_id=1),
                     'genres': Genre.objects.all(),
                     'seasons': Season.objects.all()[::-1],
                     }
        season = Season.objects.all().values()[::-1]
        print(season)
        return render(request, 'website/main.html', page_data)


class AnimeView(View):

    def get(self, request, anime_name):
        return render(request, 'website/anime_detail.html')


class WatchView(View):

    def get(self, request, anime_episode):
        return render(request, 'website/play_anime.html')

# Create your views here.
