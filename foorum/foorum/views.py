
from django.shortcuts import render
from polls.models import Question
# Create your views here.

def signup (request):
#	questions = Question.objects.all().order_by("-created_at")
#	context = {
#		"questions" : questions
#	}
	return render(request,'Kasutajad/signup.html')
