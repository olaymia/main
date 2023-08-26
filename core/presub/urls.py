from django.urls import path
from .views import *



urlpatterns = [

    path('select_subject/', select_subject, name='select_subject'),
    path('select_quantity/<int:subject_id>/', select_quantity, name='select_quantity'),
    path('start_quiz/<int:subject_id>/<int:num_questions>/', start_quiz, name='start_quiz'),
    
]
