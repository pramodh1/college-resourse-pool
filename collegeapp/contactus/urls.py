from django.urls import path
from . import views

urlpatterns = [

    path('contact1/',views.contact1,name="contact1"),
   path('postsub',views.postsub,name='postsub'),
      path('dashboard',views.dashboard,name='dashboard'),



]