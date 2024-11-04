# app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # URL барои саҳифаи асосӣ
    path('users/', views.user_list, name='user-list'),
    # URL-ҳо барои User CRUD
    path('users/', views.user_list, name='user-list'),
    path('users/create/', views.user_create, name='user-create'),
    path('users/<int:pk>/update/', views.user_update, name='user-update'),
    path('users/<int:pk>/delete/', views.user_delete, name='user-delete'),

    # URL-ҳо барои Film CRUD
    path('films/', views.film_list, name='film-list'),
    path('films/create/', views.film_create, name='film-create'),
    path('films/<int:pk>/update/', views.film_update, name='film-update'),
    path('films/<int:pk>/delete/', views.film_delete, name='film-delete'),

    # URL-ҳо барои Ticket CRUD
    path('tickets/', views.ticket_list, name='ticket-list'),
    path('tickets/create/', views.ticket_create, name='ticket-create'),
    path('tickets/<int:pk>/update/', views.ticket_update, name='ticket-update'),
    path('tickets/<int:pk>/delete/', views.ticket_delete, name='ticket-delete'),

    # URL-ҳо барои Orders CRUD
    path('orders/', views.order_list, name='order-list'),
    path('orders/create/', views.order_create, name='order-create'),
    path('orders/<int:pk>/update/', views.order_update, name='order-update'),
    path('orders/<int:pk>/delete/', views.order_delete, name='order-delete'),
]
# app/urls.py
