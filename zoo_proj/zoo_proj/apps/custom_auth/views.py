from django.http import HttpResponse
from zoo_proj.apps.custom_auth.forms.signup_form import SignupForm
from django.urls import reverse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import login


def signup(request):
    form = SignupForm()
    redirection = render(request, 'custom_auth/signup.html', {'form': form})
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            user = User.objects.create_user(
                form.cleaned_data['username'],
                form.cleaned_data['email'],
                form.cleaned_data['password'],
                last_name=form.cleaned_data['last_name'],
            )
            login(request, user)
            redirection = redirect(reverse('customauth:home'))

    return redirection


def home(request):
    return HttpResponse('<h1>HOME</h1>')