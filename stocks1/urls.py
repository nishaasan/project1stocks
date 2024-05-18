
from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('add_watchlist/', views.add_watchlist, name='add_watchlist'),
    path('add_stock/<int:watchlist_id>/', views.add_stock, name='add_stock'),
    # Add other URL patterns here
]
