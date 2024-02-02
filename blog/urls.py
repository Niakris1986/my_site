from django.urls import path
from . import views

urlpatterns = [
    path('<name_post>', views.get_post),
]
