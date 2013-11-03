# Create your views here.
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from twitai.forms import LoginForm


def index(request):
    return HttpResponse('Hello django')


def login(request):
    if request.user.is_authenticated():
        return redirect('twitai:main')
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            return HttpResponse('Great!')

    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})


@login_required()
def main(request):
    return render(request, 'main.html')


def login_error(request):
    return render(request, 'login.html', {'message' : 'You did not sign in.', 'form' : LoginForm()})


def logout(request):
    auth_logout(request)
    return redirect('twitai:login')