from django.urls import path
from apps.clients.api.api import client_api_view, client_detail_api_view

urlpatterns = [
	path('client/', client_api_view, name = 'cliente_api_view'),
	path('client/<int:pk>/', client_detail_api_view, name = 'cliente_detail_api_view')
]