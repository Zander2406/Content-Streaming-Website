from django.shortcuts import render
from django.http import HttpResponse
from django.utils.html import escape
from django.views import View


class MainView(View):

    def get(self, request):
        main_anime = {'name': 'Solo Leveling', 'episode': 6}
        popular_anime = {'name': 'Solo Leveling', 'genres': ['Action', 'Shounen', 'Adult'], 'latest_episode': 6}
        anime_name = 'Solo Leveling'
        top_anime = {'name': 'Solo Leveling', 'episode': 6}
        ongoing = 'Solo Leveling'
        genre = 'Adventure'
        page_data = {'summary': 'This is a summary',
                     'mainAnime': [main_anime for i in range(20)],
                     'popularAnime': [popular_anime for i in range(10)],
                     'recentlyAdded': [anime_name for i in range(40)],
                     'topAnime': [top_anime for i in range(10)],
                     'ongoing': [ongoing for i in range(100)],
                     'genres': [genre for i in range(83)],
                     'seasons': {2024: ['Winter'],
                                 2023: ['Winter', 'Spring', 'Summer', 'Fall'],
                                 2022: ['Winter', 'Spring', 'Summer', 'Fall'],
                                 2021: ['Winter', 'Spring', 'Summer', 'Fall'],
                                 2020: ['Winter', 'Spring', 'Summer', 'Fall'],
                                 2019: ['Winter', 'Spring', 'Summer', 'Fall'],
                                 2018: ['Winter', 'Spring', 'Summer', 'Fall'],
                                 2017: ['Winter', 'Spring', 'Summer', 'Fall'],
                                 2016: ['Winter', 'Spring', 'Summer', 'Fall'],
                                 2015: ['Winter', 'Spring', 'Summer', 'Fall'],
                                 2014: ['Winter', 'Spring', 'Summer', 'Fall']}}
        return render(request, 'website/main.html', page_data)


class AnimeView(View):

    def get(self, request, anime_name):
        return render(request, 'website/anime_detail.html')


class WatchView(View):

    def get(self, request, anime_episode):
        return render(request, 'website/play_anime.html')

# Create your views here.
