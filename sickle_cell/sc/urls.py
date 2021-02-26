from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='sickle-cell-landing-page'),
    path('stock-list/', views.stock_list, name='stock-list'),
]
