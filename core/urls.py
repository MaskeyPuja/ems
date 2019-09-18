from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

from . import views

urlpatterns = [
	path('', views.indexView, name="home"),
	path('dashboard/', views.dashboardView, name="dashboard"),
	path('login/', LoginView.as_view(), name="login_url" ),
	path('register/', views.registerView, name="register_url"),
	path('logout/', LogoutView.as_view(), name="logout"),

	path('profile-create/', views.ProfileCreateView.as_view(), name='profile_create'),
	path('profile-list/', views.ProfileListView.as_view(), name='profile_list'),
	path('profile-update/(?P<pk>[0-9]+)/$', views.ProfileUpdateView.as_view(), name='profile_update'),

	path('task-list/', views.TaskListView.as_view(), name='task_list'),
	path('task-create/', views.TaskCreateView.as_view(), name='task_create'),
	path('task-update/(?P<pk>[0-9]+)/$', views.TaskUpdateView.as_view(), name='task_update'),
	path('task-delete/(?P<pk>[0-9]+)/$', views.TaskDeleteView.as_view(), name='task_delete'),
]