from django.contrib import admin
from .models import *
from django.contrib import admin

admin.site.register(Subject)


class ChoiceAdmin(admin.StackedInline):
    model = Choice


class QuestionsAdmin(admin.ModelAdmin):
    inlines = [ChoiceAdmin]


admin.site.register(Question, QuestionsAdmin)
admin.site.register(Choice)
admin.site.register(Answer)
