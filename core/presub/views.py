from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from .models import Subject, Question, Choice


@login_required
def select_subject(request):
    subjects = Subject.objects.all()
    return render(request, 'presub/select_subject.html', {'subjects': subjects})


@login_required
def select_quantity(request, subject_id):
    subjects = Subject.objects.get(id=subject_id)
    return render(request, "presub/select_quantity.html", {'subjects': subjects})


@login_required
def start_quiz(request, subject_id, num_questions):
    subjects = Subject.objects.get(id=subject_id)
    questions = Question.objects.filter(id=subject_id).order_by('?')[:num_questions]
    choices = Choice.objects.filter(question__in=questions)
    return render(request, 'presub/start_quiz.html', {'subjects': subjects, 'questions': questions, 'choices': choices})



# @login_required
#  def submit_answer(request, subject_id, question_id):
 #   if request.method == 'POST':
 #       user_answer = request.POST.get('user_answer')
  #      question = get_object_or_404(Question, id=question_id)
   #     # Save user_answer to the database or session
   #     # Move to the next question or show results if all questions are answered
   #     return redirect('next_question_or_results', subject_id=subject_id)


#@login_required
#def next_question_or_results(request, subject_id):
    # Determine whether to show the next question or display quiz results
    # Retrieve user answers from the database or session
    # Compare user answers with correct choices
    # Calculate the score and other relevant information
    # return render(request, 'presub/quiz_results.html', {'score': score})






