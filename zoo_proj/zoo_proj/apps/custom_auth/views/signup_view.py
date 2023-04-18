from zoo_proj.apps.custom_auth.forms import SignupForm
from django.urls import reverse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import login


def signup_view(request):
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