from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    # path('home', views.home, name='home'),
    # path('list_balai', views.list_balai, name='list_balai'),
    # path('add_paket', views.add_paket, name='add_paket'),
    # path('list_paket', views.list_paket, name='list_paket'),
]
