# Create your views here.
from django.http.response import HttpResponse
from django.shortcuts import render
from twitai.forms import LoginForm


def index(request):
    return HttpResponse('Hello django')


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            return HttpResponse('Great!')

    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})


def loginSuccess(request):
    return HttpResponse('SUCCESS')


def loginError(request):
    return render(request, 'login.html', {'message' : 'You did not sign in.', 'form' : LoginForm()})


def secret(request):
    return HttpResponse('Secret!')