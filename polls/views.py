from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Question
from django.template import loader
from django.shortcuts import render
# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    # return HttpResponse(template.render(context, request))

    # render(request, templates_name, context=None, content_type=None, status=None, using=None)
    return render(request, 'polls/index.html', context)

def detail(requset, question_id):
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404('Question does not exist.')

    # get_object_or_404(model, **kwargs)
    question = get_object_or_404(Question, pk=question_id)
    return render(requset, 'polls/detail.html', {'question': question})

def result(requset, question_id):
    response = 'You are looking at the result of the question %s.'
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse('You are voting on the question %s.' % question_id)


