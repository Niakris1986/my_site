from django.urls import path
from . import views

urlpatterns = [
    path('<int:name_post>', views.get_post_by_number),
    path('<str:name_post>', views.get_post),
]
