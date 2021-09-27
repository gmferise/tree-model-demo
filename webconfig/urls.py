"""webconfig URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from website import views as site

urlpatterns = [
    path('admin/', admin.site.urls),

    path('signup/', site.Signup.as_view(), name='signup'),
    path('login/', site.Login.as_view(), name='login'),
    path('logout/', site.Logout.as_view(), name='logout'),

    path('', site.Home.as_view(), name='home'),
    path('new/file/<int:in_id>/', site.CreateFile.as_view(), name='create_file'),
    path('new/folder/<int:in_id>/', site.CreateFolder.as_view(), name='create_folder'),
]
