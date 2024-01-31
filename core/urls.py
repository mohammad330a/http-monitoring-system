from django.urls import path, re_path
from core import views

urlpatterns = [
    path('server-register/', views.ServerRegisterAPI.as_view(), name='server-register'),
    re_path(r'^server-status(?P<pj>.+)$', views.ServerStatusAPI.as_view(), name='server-status'),
    path('server-list/', views.ServerListAPI.as_view(), name='server-list'),
]
