from django.urls import path
from task import views

app_name = 'task'

urlpatterns = [
	path('', views.index, name="index"),
    path('home/', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.handlelogin, name='handlelogin'),
    path('logout/', views.handlelogout, name='handlelogout'),
    path('addtask', views.addTask, name="addtask"),
    path('editTask/<int:task_id>/', views.editTask, name='editTask'),
    path('calender', views.calender, name='calender')
]