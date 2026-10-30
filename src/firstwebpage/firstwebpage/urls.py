from django.contrib import admin
from django.urls import path
from flatpages import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    path("hello/", views.hello, name="hello"),
    path("hello/plain/", views.hello_plain, name="hello_plain"),
    path("template/", views.template_page, name="template_page"),
]
