from django.urls import path
from . import views

app_name = 'groups'

urlpatterns = [
    path('', views.ListGroups.as_view(), name='all'),
    path('new/', views.CreateGroup.as_view(), name='create'),
    path('posts/in/<slug>/', views.SingleGroup.as_view(), name='single'),
    path('join/<slug>/', views.JoinGroup.as_view(), name='join'),
    path('leave/<slug>/', views.LeaveGroup.as_view(), name='leave'),

]

# if this doesn't work try setting it to <slug:slug>
# I think because the 'slug' is already a slug I
# don't have to specify to turn it into one but
# I could be wrong
