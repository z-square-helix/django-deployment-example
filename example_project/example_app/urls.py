from django.urls import path

from example_app import views

# Template Tagging
app_name = 'example_app'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('users/', views.users, name = 'users'),
    path('forms/', views.forms_view, name = 'forms'),
    path('signup/', views.signup_form, name = 'signup'),
    path('relative/', views.relative, name = 'relative'),
    path('child/', views.child, name = 'child'),
    path('register/', views.register, name = 'register'),
    path('user_logout/', views.user_logout, name = 'user_logout'),
    path('user_login/', views.user_login, name = 'user_login'),
]
