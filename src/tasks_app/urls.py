from . import views
from django.urls import path

app_name = "tasks_app"

urlpatterns = [
    path('', views.home, name="home"),
    path("delete", views.delete, name="delete"),
    # path('testcookie/', views.cookie_session, name="test_cookie"),
    # path('deletecookie/', views.cookie_delete, name="delete_cookie"),

]


