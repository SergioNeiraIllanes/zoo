from typing import Any
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from django.http import HttpRequest, HttpResponse
from zoo_proj.apps.custom_auth.forms import PermissionCreateForm
from django.urls import reverse
from django.shortcuts import redirect, render
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType



class PermissionCreateView(LoginRequiredMixin, View):
    template_name = 'custom_auth/permission_create_view.html'

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        form = PermissionCreateForm()
        redirection = render(
            request,
            self.template_name,
            {
                'form': form,
            }
        )
        return redirection
        

    def post(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        form = PermissionCreateForm(self.request.POST)
        redirection = render(
            request,
            self.template_name,
            {
                'form': form,
            }
        )
        if form.is_valid():
            Permission.objects.create(
                name=form.cleaned_data['name'],
                codename=form.cleaned_data['codename'],
                content_type=ContentType.objects.get(
                    pk=form.cleaned_data['content_type'],
                )
            )
            redirection = redirect(reverse('customauth:permission-list'))
            

        return redirection