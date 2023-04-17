from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.contrib.auth.models import Permission


class PermissionListView(LoginRequiredMixin, generic.ListView):
    model = Permission
    template_name = 'custom_auth/permission_list.html'
    context_object_name = 'permissions'