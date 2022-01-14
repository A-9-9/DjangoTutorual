from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Question, Choice
from django.shortcuts import render
from django.urls import reverse
from django.db.models import F
from django.views import generic

# For ListView, automatically generated context variable is question_list.
# We can change the templates to match the new default context variables,
# or tell Django to use the variable you want. Default(question_list)
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]

# DetailView needs pk value
# The template_name attribute is used to tell Django to use a specific
# template name instead of the autogenerated default template name.
# Default:<app name>/<model name>_detail.html
class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/result.html'


#
# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     # template = loader.get_template('polls/index.html')
#     context = {
#         'latest_question_list': latest_question_list,
#     }
#     # return HttpResponse(template.render(context, request))
#
#     # render(request, templates_name, context=None, content_type=None, status=None, using=None)
#     return render(request, 'polls/index.html', context)
#
# def detail(requset, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(requset, 'polls/detail.html', {'question': question})
#
# def result(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/result.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': 'You didn\'t select a choice.'
        })
    else:
        selected_choice.votes = F('votes') + 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:result', args=(question_id,)))



