from django.urls import path
from . import views
from django.contrib.auth import views as auth_views



urlpatterns=[
    path('add',views.add,name='add'),
    path('calc',views.calc,name='calc'),
    path('',views.home,name="home"),
      path('login',views.signin,name='login'),
    path('register',views.register,name="register"),
       path('logout/', views.logout_view, name='logout'),


]