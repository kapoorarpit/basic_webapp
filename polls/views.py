from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from django.http import Http404
from django.shortcuts import get_object_or_404,render
from .models import Question,choice
from django.template import loader
from django.urls import reverse
from django.views import generic
from django.utils import timezone

class index(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_list'

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte =timezone.now()).order_by('-pub_date')[:5]

class detail(generic.DetailView):
    template_name = 'polls/detail.html'
    model = Question
    
    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now())

class results(generic.DetailView):
    template_name = 'polls/results.html'
    model = Question

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


