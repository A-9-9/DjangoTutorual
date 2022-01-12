from django.urls import path
from . import views
# put the route related with views
urlpatterns = [
    path('', views.index, name='index'),
]