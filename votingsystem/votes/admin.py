from django.contrib import admin
from .models import Question, Option
# Register your models here.


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    pass


@admin.register(Option)
class OptionAdmin(admin.ModelAdmin):
    list_display = ("option_text", "question", "votes")
    
