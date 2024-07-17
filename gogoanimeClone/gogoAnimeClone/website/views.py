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
                     'top_anime': Episodes.objects.order_by("comments"),
                     'ongoing': Anime.objects.filter(status_id=1),
                     'genres': Genre.objects.all(),
                     'seasons': Season.objects.all()[::-1],
                     }
        return render(request, 'website/main.html', page_data)


class AnimeView(View):

    def get(self, request, anime_name):
        recent_releases = Episodes.objects.all()
        page_data = {'anime_details': Anime.objects.filter(name_slug=anime_name)[0],
                     'genres': GenreMap.objects.filter(anime__name_slug=anime_name),
                     'episodes': Episodes.objects.filter(anime__name_slug=anime_name),
                     'seasons': Season.objects.all()[::-1],
                     'latest_episodes': recent_releases[len(recent_releases) - 60:][::-1],
                     }
        return render(request, 'website/anime_detail.html', page_data)


class WatchView(View):

    def get(self, request, anime_episode):
        name_components = anime_episode.split('-')
        episode_number = name_components[-2:]
        episode_number[0] = episode_number[0].capitalize()
        episode_number = ' '.join(episode_number)
        del name_components[-2:]
        anime_name = name_components
        anime_name = '-'.join(anime_name)
        episodes = Episodes.objects.filter(anime__name_slug=anime_name)
        recent_releases = Episodes.objects.all()
        current_episode = None
        prev_episode = None
        next_episode = None
        for i in range(len(episodes)):
            if episodes[i].name == episode_number:
                current_episode = episodes[i]
                if i - 1 >= 0:
                    prev_episode = episodes[i - 1]
                if i + 1 < len(episodes):
                    next_episode = episodes[i + 1]
        page_data = {'related_episodes': episodes,
                     'current_episode': current_episode,
                     'prev_episode': prev_episode,
                     'next_episode': next_episode,
                     'latest_episodes': recent_releases[len(recent_releases) - 60:][::-1],
                     'seasons': Season.objects.all()[::-1],
                     }
        return render(request, 'website/play_anime.html', page_data)


class GenreView(View):

    def get(self, request, genre):
        return render(request, 'website/play_anime.html')

