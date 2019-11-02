from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from django.views import generic
from .models import Experience


class IndexView(generic.ListView):
    template_name = 'cv/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Experience.objects.order_by('-start_date')[:5]

# def index(request):
#     latest_question_list = Experience.objects.order_by('-start_date')[:5]
#     template = loader.get_template('cv/index.html')
#     context = {
#         'latest_question_list': latest_question_list,
#     }
#     return HttpResponse(template.render(context, request))

    # latest_exp_list = Experience.objects.order_by('-start_date')[:5]
    # output = ', '.join([q.title for q in latest_exp_list])
    # return HttpResponse(output)


    # return HttpResponse("Hello, world. You're at the polls index.")

# def detail(request, question_id):
#     return HttpResponse("You're looking at question %s." % question_id)
#
#
# def results(request, question_id):
#     response = "You're looking at the results of question %s."
#     return HttpResponse(response % question_id)
#
#
# def vote(request, question_id):
#     return HttpResponse("You're voting on question %s." % question_id)
