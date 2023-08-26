from django.urls import path
from .views import *


urlpatterns = [
    path('select_topic/', select_topic, name='select_topic'),
    path('select_topic_quantity/<int:topic_id>/', select_topic_quantity, name='select_topic_quantity'),
    path('start_topic_quiz/<int:topic_id>/<int:num_questions>/', start_topic_quiz, name='start_topic_quiz'),
]
