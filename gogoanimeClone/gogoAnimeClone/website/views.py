from django.shortcuts import render
from django.http import HttpResponse
from django.utils.html import escape
from django.views import View


class MainView(View):

    def get(self, request):
        main_anime = {'name': 'Solo Leveling', 'episode': 6}
        popular_anime = {'name': 'Solo Leveling', 'genres': ['Action', 'Shounen', 'Adult'], 'latest_episode': 6}
        page_data = {'summary': 'This is a summary',
                     'mainAnime': [main_anime for x in range(1, 21)],
                     'popularAnime': [popular_anime for i in range(1, 11)]}
        return render(request, 'website/main.html', page_data)


class AnimeView(View):

    def get(self, request, anime_name):
        return render(request, 'website/anime_detail.html')


class WatchView(View):

    def get(self, request, anime_episode):
        return render(request, 'website/play_anime.html')

# Create your views here.
