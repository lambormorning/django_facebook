"""main URL Configuration

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
from django.urls import path
from facebook.views import play
from facebook.views import play2
from facebook.views import profile
from facebook.views import week3
from facebook.views import newsfeed
from facebook.views import detail_feed
from facebook.views import new_feed
from facebook.views import remove_feed
from facebook.views import edit_feed
from facebook.views import new_page


urlpatterns = [
    path('admin/', admin.site.urls),
    path('play', play),
    path('play2', play2),
    path('myname/profile/dsfasdfasdf', profile),  # 앞의 경로로 들어오면, 뒤에 함수를 호출해라
    path('week3', week3),
    path('', newsfeed),git
    path('feed/<pk>/', detail_feed),
    path('feed/<pk>/remove/', remove_feed),
    path('feed/<pk>/edit/', edit_feed),
    path('new/', new_feed),
    path('pages/new/', new_page),
    ]
