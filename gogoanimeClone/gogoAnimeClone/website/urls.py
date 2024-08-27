from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = "website"
urlpatterns = [
    path('', views.MainView.as_view()),
    path('category/<slug:anime_name>', views.AnimeView.as_view(), name='anime_detailed_view'),
    path('<slug:anime_episode>', views.WatchView.as_view(), name='episode_view'),
    path('genre/<slug:genre_name>', views.GenreView.as_view(), name='genre_view'),
    path('anime-list.html', views.AnimeListView.as_view(), name='anime_list_view'),
]
