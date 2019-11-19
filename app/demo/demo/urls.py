"""demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

from home.views import index, link_list, link_detail, link_redirect, start_presentation

urlpatterns = [
    path("admin/", admin.site.urls),
    path("links/", link_list, name="link-list"),
    path("links/<int:link_id>/", link_detail, name="link-detail"),
    path("links/<int:link_id>/redirect/", link_redirect, name="link-redirect"),
    path("start/", start_presentation, name="start-presentation"),
    path("", index, name="index"),
]
