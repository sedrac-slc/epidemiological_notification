from django.urls import path, include
from core.enum.link import LinkEnum
from . import views

urlpatterns = [
    path('', views.index, name = LinkEnum.DEFAULT_HOME.get()),
    path('login/', views.login, name = LinkEnum.DEFAULT_LOGIN.get())
]