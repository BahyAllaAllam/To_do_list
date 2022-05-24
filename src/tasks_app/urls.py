from . import views
from django.urls import path

app_name = "tasks_app"

urlpatterns = [
    path('', views.home, name="home"),
    path("add", views.add, name="add"),
    path("delete", views.delete, name="delete"),
    path('testcookie/', views.cookie_session),
    path('deletecookie/', views.cookie_delete),

]


