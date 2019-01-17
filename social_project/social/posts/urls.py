from django.urls import path

from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.PostList.as_view(), name='all'),
    path('new/', views.CreatePost.as_view(), name='create'),
    path('by/<username>/', views.UserPosts.as_view(), name='for_user'),
    path('by/<username>/<int:pk>/', views.PostDetail.as_view(), name='single'),
    path('delete/<int:pk>/', views.DeletePost.as_view(), name='delete'),
]

# if this doesn't work try setting it to <str:username>
# I think because the 'username' is already a string I 
# don't have to specify to turn it into one but
# I could be wrong
