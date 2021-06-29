from django.urls import path
from . import views

urlpatterns = [
    path('discussion',views.discussion,name="discussion"),
]
