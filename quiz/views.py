from django.shortcuts import render
from django.http import Http404, HttpResponse
from django.template import loader

from .models import Quiz

# Create your views here.
def index(request):
    quizes_list = Quiz.objects.order_by('-subject')
    template = loader.get_template('quiz/index.html')
    context = {
        'quizes_list': quizes_list
    }
    return HttpResponse(template.render(context, request))

def detail(request, quiz_id):
    try:
        quiz = Quiz.objects.get(pk=quiz_id)
    except Quiz.DoesNotExist:
        raise Http404("Опитування не існує")
    return render(request, 'quiz/detail.html', {'quiz': quiz})

def answer(request, quiz_id):
    try:
        quiz = Quiz.objects.get(pk=quiz_id)
    except Quiz.DoesNotExist:
        raise Http404("Опитування не існує")
    return render(request, 'quiz/detail.html', {'quiz': quiz})