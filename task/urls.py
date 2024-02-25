from django.urls import path
from task import views

urlpatterns = [
	path('', views.index, name="index"),
    path('home/', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.handlelogin, name='handlelogin'),
    path('logout/', views.handlelogout, name='handlelogout'),
    path('addtask', views.addTask, name="addtask"),
]