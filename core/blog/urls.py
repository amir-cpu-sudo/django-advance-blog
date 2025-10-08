from django.urls import path, include
from .views import *

app_name = 'blog'

urlpatterns = [
    path('api/',include('blog.api.urls'))
]