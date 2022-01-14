from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
from django.shortcuts import render
# Create your views here.
def index(request):
    latest_question_list = Question.objects.all()[:5]
    return render(request, 'polls/index.html', {'latest_question_list': latest_question_list})
    # return HttpResponse('Hello, world. You are in the polls index.')
