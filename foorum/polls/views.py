
from django.shortcuts import render
from django.template import loader
from django.views import generic
from .models import Question, Response
from django.http import HttpResponse

#def IndexView(request):
#    template = loader.get_template('polls/index.html')
#    questions = Question.objects.all().values()
#    context = {
#        'questions': questions,
#    }
#    return HttpResponse(template.render(context, request))


# Create your views here.

