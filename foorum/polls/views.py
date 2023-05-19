<<<<<<< HEAD
=======
from django.shortcuts import render
from django.template import loader
from django.views import generic
from .models import Question, Response
from django.http import HttpResponse

def IndexView(request):
    template = loader.get_template('polls/index.html')
    kusimus = Question.objects.all().values()
    context = {
        'kusimus': kusimus,
    }
    return HttpResponse(template.render(context, request))


# Create your views here.
>>>>>>> c79c9e29db5d2afdb599260b32da05962ef9fadc
