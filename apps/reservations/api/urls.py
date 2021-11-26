from django.urls import path
from apps.reservations.api.views.general_views import RoomsListAPIView
from apps.reservations.api.views.reservation_views import ReservationListAPIView,ReservationCreateAPIView,ReservationRetrieveAPIView,ReservationDestroyAPIView,ReservationUpdateAPIView

urlpatterns = [
	path('rooms/', RoomsListAPIView.as_view(), name = 'rooms'),
	path('reservation/list/', ReservationListAPIView.as_view(), name = 'reservation_list'),
	path('reservation/create/', ReservationCreateAPIView.as_view(), name = 'reservation_create'),
	path('reservation/retrieve/<int:pk>/', ReservationRetrieveAPIView.as_view(), name = 'reservation_retrieve'),
	path('reservation/destroy/<int:pk>/', ReservationDestroyAPIView.as_view(), name = 'reservation_destroy'),
	path('reservation/update/<int:pk>/', ReservationUpdateAPIView.as_view(), name = 'reservation_update')
]