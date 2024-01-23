from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = "website"
urlpatterns = [
    path('', views.MainView.as_view()),
    path('category/<str:anime_name>', views.AnimeView.as_view(), name='anime_detailed_view'),
    path('<str:anime_episode>', views.WatchView.as_view(), name='episode_view')
]
