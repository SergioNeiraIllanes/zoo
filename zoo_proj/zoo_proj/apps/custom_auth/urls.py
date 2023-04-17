from django.urls import path
from .views import signup, home


app_name = 'customauth'

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('home/', home, name='home')
]