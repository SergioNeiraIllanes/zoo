from django.urls import path
from zoo_proj.apps.custom_auth.views import (
    signup_view,
    home_view,
    PermissionListView,
    PermissionDetailView,
    PermissionDeleteView,
)


app_name = 'customauth'

urlpatterns = [
    path('signup/', signup_view, name='signup'),
    path('home/', home_view, name='home'),
    path(
        'permission/',
        PermissionListView.as_view(),
        name='permission-list',
    ),
    path(
        '<int:pk>/permission-detail/',
        PermissionDetailView.as_view(),
        name='permission-detail',
    ),
    path(
        'permission-delete/',
        PermissionDeleteView.as_view(),
        name='permission-delete',
    )
]