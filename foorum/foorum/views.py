
from django.shortcuts import render
from polls.models import Question, Response
from django.http import HttpResponse
from django.template import loader

# Create your views here.


def signup (request):
#	questions = Question.objects.all().order_by("-created_at")
#	context = {
#		"questions" : questions
#	}
	return render(request,'Kasutajad/signup.html')

def IndexView(request):
    template = loader.get_template('index.html')
    questions = Question.objects.all().values()
    context = {
        'questions': questions,
    }
    return HttpResponse(template.render(context, request))
