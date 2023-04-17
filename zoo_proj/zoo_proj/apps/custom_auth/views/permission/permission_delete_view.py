from typing import Any
from django.views.generic import View
from django.contrib.auth.models import Permission
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect
from django.urls import reverse


class PermissionDeleteView(View):

    def post(request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        pk = request.request.POST['id']
        permission = Permission.objects.get(pk=pk)
        permission.delete()
        return redirect(reverse('customauth:permission-list'))
