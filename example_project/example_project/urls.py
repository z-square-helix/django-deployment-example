"""example_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from example_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('example_app.urls')),
]

# the path '' means anything will look at the app
# level urls file to see if there is a direction there
# I can change this to look at different app url
# files depending on the path in the form of 'name/'
# for example to look at second app I can say
# path('second_app/', include('second_app.urls')),
# I can also add a view that is not in urls.py by
# using the form path('name/', views.name, name = 'name')
