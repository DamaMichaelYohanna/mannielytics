from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('login/', views.admin_login, name='admin_login'),
    path('logout/', views.admin_logout, name='admin_logout'),
    path('courses/', views.manage_courses, name='manage_courses'),
    path('courses/add/', views.add_course, name='add_course'),
    path('courses/<int:pk>/edit/', views.edit_course, name='edit_course'),
    path('courses/<int:pk>/delete/', views.delete_course, name='delete_course'),
    path('messages/', views.messages_list, name='messages_list'),
    path('messages/<int:pk>/delete/', views.delete_message, name='delete_message'),
    path('team/', views.manage_team, name='manage_team'),
    path('team/add/', views.add_team_member, name='add_team_member'),
    path('team/<int:pk>/edit/', views.edit_team_member, name='edit_team_member'),
    path('team/<int:pk>/delete/', views.delete_team_member, name='delete_team_member'),
]

