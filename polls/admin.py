from django.contrib import admin
from .models import Question, Choice
# Register your models here.
# register models that admin site can mapping your models
admin.site.register(Question)
admin.site.register(Choice)