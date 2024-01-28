from django.urls import path
from . import views

urlpatterns = [
    
    path('',views.home,name = 'home'),
    path('login/',views.user_login,name = 'login'),
    path('signup/',views.SignUp,name = 'signup'),
    path('profile/',views.Profile,name = 'profile'),
    path('logout/',views.User_logout,name = 'logout'),
    path('pass1/',views.passchng,name = 'pass1'),
    path('pass2/',views.passchngWO,name = 'pass2'),
]