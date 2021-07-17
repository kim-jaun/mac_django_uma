from django.shortcuts import render
from .models import Question



def index(request):
    """
    login 모델 출력
    """
    question_list = Question.objects.order_by('-create_date')
    context = {'question_list': question_list}
    return render(request, 'login/question_list.html', context)