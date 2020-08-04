"""taskapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from myapp import views
from .router import router
from rest_framework.authtoken import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('profiledetail/',views.ProfileDetail.as_view(),name='profile_detail'),
    #api related path

    path('profile/<slug:username>/',views.ProfileView.as_view()),
    path('api/',include(router.urls)),
    path('api-token-auth/',auth_views.obtain_auth_token, name='api-token-auth'),
    # path('profile/<username:username>',views.ProfileView.as_view(),name='profileview'),
    #http post http://localhost:8000/api-token-auth/ username=vikas password=Python@123
    
    # path('api/auth/',include('djoser.urls.authtoken')),
    # path('api_login',views.ExampleView.as_view(),name='api_login'),

    #Normal user Path

    path('index/',views.Index.as_view(),name='home'),
    path('user_login',views.LoginView.as_view(template_name='myapp/login.html'), name='login'),
    path('user_logout',views.LogoutView.as_view(),name='logout'),
    
    

]
