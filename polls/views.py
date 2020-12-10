from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from django.http import Http404
from django.shortcuts import get_object_or_404,render
from .models import Question,choice
from django.template import loader
from django.urls import reverse

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
        question = get_object_or_404(Question, pk= question_id)
        return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        s_choice = question.choice_set.get(pk=request.POST['choice'])
    except(KeyError, choice.DoesNotExist):
        return render(request, 'polls/detail.html', {'question': question, 'error_message': "You did'nt selected any choice"})
    else:
        s_choice.votes +=1
        s_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))


