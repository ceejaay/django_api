from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # template = loader.get_template('polls/index.html')
    context = {
            'latest_question_list': latest_question_list,
            }
    # output = ', '.join([q.question_text for q in latests_question_list])
    return render(request, 'polls/index.html', context)

def things(request):
    return HttpResponse("this is the things urlndex")

def detail(request, question_id):
    # I ended on this part of the tutorial
    # https://docs.djangoproject.com/en/3.1/intro/tutorial03/#a-shortcut-get-object-or-404
    # try:
        question = get_object_or_404(Question, pk=question_id)
        return render(request, 'polls/details.html', {'question': question} )
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist.")
    # return render(request, 'polls/details.html', {'question': question})


def results(request, question_id):
    response = "Your're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
# Create your views here.
