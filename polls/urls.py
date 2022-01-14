from django.urls import path
from . import views
# put the route related with views
# colon separates the converter and the pattern name -> <int:question_id>, <str:text>
app_name = 'polls'
# when html invoke the 'url', can differentiate the name with other apps like app_name: name
urlpatterns = [

    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results', views.ResultsView.as_view(), name='result'),
    path('<int:question_id>/vote', views.vote, name='vote')
]