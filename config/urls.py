from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path("admin/", admin.site.urls), # , namespace=""
    path("todo/", include("todo.urls")),
    path("", lambda request: redirect("todo_List")), # 127.0.0.1:8000/
    path("api-auth/", include("rest_framework.urls")), 

]
