from django.urls import path
from . import views

urlpatterns = [
    path('<str:name_post>', views.get_post),
]
