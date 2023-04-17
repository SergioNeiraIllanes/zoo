from typing import Any
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import Permission
from django.http import HttpRequest, HttpResponse


class PermissionDetailView(LoginRequiredMixin, DetailView):
    model = Permission
    template_name = 'custom_auth/permission_detail_view.html'
