from django.urls import path
from .views import *


urlpatterns = [

    path('select_semester/', select_semester, name='select_semester'),
    path('select_semester_quantity/<int:semester_id>/', select_semester_quantity, name='select_semester_quantity'),
    path('start_semester_quiz/<int:semester_id>/<int:num_questions>/', start_semester_quiz, name='start_semester_quiz'),


]