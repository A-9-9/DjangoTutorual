from django.urls import path
from . import views
# put the route related with views
# colon separates the converter and the pattern name -> <int:question_id>, <str:text>
app_name = 'polls'
# when html invoke the 'url', can differentiate the name with other apps like app_name: name
urlpatterns = [
    # /polls/
    path('', views.index, name='index'),
    # /polls/2/
    path('<int:question_id>/', views.detail, name='detail'),
    # /polls/2/results
    path('<int:question_id>/results', views.result, name='result'),
    # /polls/2/vote
    path('<int:question_id>/vote', views.vote, name='vote')
]