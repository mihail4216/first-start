from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render_to_response


def base(request):
    return render(request, 'Blog/base.html')
def home(request):
    return render(request,'Blog/home.html')
def register(request):
    return render(request,'Blog/register.html')