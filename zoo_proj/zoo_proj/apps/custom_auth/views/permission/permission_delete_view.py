from django.contrib.auth.mixins import LoginRequiredMixin
from typing import Any
from django.views.generic import View
from django.contrib.auth.models import Permission
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect
from django.urls import reverse


class PermissionDeleteView(LoginRequiredMixin, View):

    def post(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        pk = self.request.POST['id']
        permission = Permission.objects.get(pk=pk)
        permission.delete()
        return redirect(reverse('customauth:permission-list'))
