# -*- coding: utf-8 -*-


from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from django.contrib import auth

from Blog.models import Question


def base(request):

    return render(request, 'Blog/base.html')
def home(request):
    return render(request,'Blog/home.html')
def register(request):
    return render(request,'Blog/register.html')


def login(request):
    username = request.POST.get('username',False)
    password = request.POST.get('password',False)
    user = auth.authenticate(username=username, password=password)
    if user :
        auth.login(request,user)
    else:
        return render_to_response('Blog/login.html')
def logout(request):
    auth.logout(request)
    return render_to_response('Blog/logout.html')


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)


def detail(request, question_id):
    return render_to_response('Blog/detail.html')


def vote(request, question_id):
    return render_to_response('Blog/vote.html')


