from django.shortcuts import render
from django.http import HttpResponse
from django.utils.html import escape
from django.views import View
from .models import *
from django.core.paginator import Paginator


class MainView(View):

    def get(self, request):
        latest_episodes = Episodes.objects.all()[::-1]
        latest_ep_paginator = Paginator(latest_episodes, 20)
        latest_ep_page_number = request.GET.get("page")
        latest_ep_page_object = latest_ep_paginator.get_page(latest_ep_page_number)

        popular_anime = Anime.objects.order_by("rating")
        popular_anime_paginator = Paginator(popular_anime, 10)
        popular_anime_page_number = request.GET.get("page")
        popular_anime_page_object = popular_anime_paginator.get_page(popular_anime_page_number)
        page_data = {'latest_episodes': Episodes.objects.all()[::-1],
                     'popular_anime': Anime.objects.order_by("rating"),
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

# Create your views here.
