from django.urls import path
from . import views


urlpatterns =[
    path('',views.home,name="home"),
    path('about',views.about,name="about"),
    path('services',views.services,name="services"),
    path('contact',views.contact,name="contact"),
    path('daa',views.daa,name="daa"),
    path('unix',views.unix,name="unix"),
    path('java',views.java,name="java"),
    path('python',views.python,name="python"),
    path('post',views.post,name="post"),
    path('interview',views.interview,name="interview"),
    path('coding',views.coding,name="coding"),
    path('development',views.development,name="development"),
]