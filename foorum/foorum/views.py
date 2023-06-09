
from django.shortcuts import render
from polls.models import Question, Response
from django.http import HttpResponse
from django.template import loader
from django.urls import reverse
from django.views import generic
# Create your views here.


def signup (request):

	return render(request,'Kasutajad/signup.html')

def IndexView(request):
    template = loader.get_template('home.html')
    questions = Question.objects.all().order_by("-id").values()
    context = {
        'questions': questions,
    }
    return HttpResponse(template.render(context, request))

def tuhjusView(request, pk):
    question = Question.objects.filter(id=pk)
    context = {
        'question': question,
    }
    return render(request, 'tuhjus.html', context)
