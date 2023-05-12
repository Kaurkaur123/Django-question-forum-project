from django.shortcuts import render
from django.template import loader
from django.views import generic
from .models import Question, Response
from django.http import HttpResponse

class IndexView(generic.Listview):
    template = loader.get_template('polls/index.html')
    kusimus = Question.objects.all().values()
    context = {
        'kusimus': kusimus,
    }


# Create your views here.
