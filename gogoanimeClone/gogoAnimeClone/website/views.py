from django.shortcuts import render
from django.http import HttpResponse
from django.utils.html import escape
from django.views import View


class MainView(View):

    def get(self, request):
        return render(request, 'website/main.html')

# Create your views here.
