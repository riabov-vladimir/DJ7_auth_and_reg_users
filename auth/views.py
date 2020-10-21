# from django.contrib.auth.forms import UserCreationForm

from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from auth.forms import UserCreationForm


def home(request):
    return render(
        request,
        'home.html'
    )


def register(request):
    if request.method == 'POST':
        f = UserCreationForm(request.POST)
        if f.is_valid():
            f.save()
            return redirect('home')

    else:
        f = UserCreationForm()

    return render(request, 'signup.html', {'form': f})
