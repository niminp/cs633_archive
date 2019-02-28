from django.urls import path, re_path
from django.conf.urls import url
from django.shortcuts import render
# import django_saml2_pro_auth.views
import manager.views as views

urlpatterns = [
	path('', views.main, name='main'),
	path('auth/login/', views.login_user, name='login'),
	path('auth/logout/', views.logout_user, name='logout'),
	path('project/<int:project_id>/', views.project, name='project'),
	path('project/hide/<int:project_id>/', views.hide_project, name='hide_project'),
	path('project/show/<int:project_id>/', views.show_project, name='show_project'),
	path('project/delete/<int:project_id>/', views.delete_project, name='delete_project'),
	path('project/search/', views.search, name='search'),
	path('project/upload/', views.upload, name='upload'),
]