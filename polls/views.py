from django.http import HttpResponse, Http404,HttpResponseRedirect
from django.shortcuts import render, get_object_or_404


# Create your views here.
from django.template import loader
from django.urls import reverse
from django.views import generic

from polls.models import Question,Choice
from django.shortcuts import render

class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        return Question.objects.order_by("-pub_date")[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"

class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"

def index(request):
    # return HttpResponse("hello,world. by polls index.")
    # 排序，倒序排发布日期，取前5个
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    print(latest_question_list, type(latest_question_list))
    context = {
        'latest_question_list':latest_question_list
    }
    # \n没用？
    #output = ','.join([q.question_text for q in latest_question_list])
    # return HttpResponse(output)

    # 写法二
    # template = loader.get_template("polls/index.html")
    # return HttpResponse(template.render(context, request))

    # 写法三
    return render(request, "polls/index.html", context)

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question %s does not exist!!!" % question_id)
    return render(request, "polls/detail.html", {"question":question})

    # 写法二
    # response = "you're looking at the results of question %s."
    # return HttpResponse(response % question_id)

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request,"polls/detail.html",{
            "question":question,
            "error_message":"you did not select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))


    # 写法二
    # return HttpResponse("you're voting on question %s." % question_id)

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return  render(request, "polls/results.html", {
        "question":question
    })

    # 二
    # response = "you're looking at the results of question %s."
    # return HttpResponse(response % question_id)