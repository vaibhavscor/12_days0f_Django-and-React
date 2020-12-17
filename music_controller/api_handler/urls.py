from django.urls import path
from . import views

urlpatterns = [
    path('', views.Roomview.as_view(), name="room")
]
