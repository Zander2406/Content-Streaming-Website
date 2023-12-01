from django.shortcuts import render
from django.http import HttpResponse
from django.utils.html import escape
from django.views import View


class MainView(View):

    def get(self, request):
        return render(request, 'website/main.html')


class AnimeView(View):

    def get(self, request, anime_name):
        return render(request, 'website/anime_detail.html')


class WatchView(View):

    def get(self, request, anime_name):
        return render(request, 'website/play_anime.html')

# Create your views here.
