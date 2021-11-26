from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response

from apps.base.api import GeneralListApiView
from apps.reservations.api.serializers.reservation_serializers import ReservationSerializer

class ReservationListAPIView(GeneralListApiView):
	serializer_class = ReservationSerializer

class ReservationCreateAPIView(generics.CreateAPIView):
	serializer_class = ReservationSerializer

	def post(self, request):
		serializer = self.serializer_class(data = request.data)
		if serializer.is_valid():
			serializer.save()
			return Response({'message': 'Reservación creada correctamente'}, status = status.HTTP_201_CREATED)
		return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class ReservationRetrieveAPIView(generics.RetrieveAPIView):
	serializer_class = ReservationSerializer
	def get_queryset(self):
		return self.get_serializer().Meta.model.objects.filter(sw = True)

class ReservationDestroyAPIView(generics.DestroyAPIView):
	serializer_class = ReservationSerializer
	def get_queryset(self):
		return self.get_serializer().Meta.model.objects.filter(sw = True)

	def delete(self, request, pk=None):
		reservation = self.get_queryset().filter(id = pk).first()
		if reservation:
			reservation.sw = False
			reservation.save()
			return Response({'message': 'Reservación eliminada correctamente'}, status = status.HTTP_200_OK)
		return Response({'error': 'No existe una Reservación con estos datos'}, status = status.HTTP_400_BAD_REQUEST)

class ReservationUpdateAPIView(generics.UpdateAPIView):
	serializer_class = ReservationSerializer

	def get_queryset(self, pk):
		return self.get_serializer().Meta.model.objects.filter(sw = True).filter(id = pk).first()

	def patch(self, request, pk=None):
		if self.get_queryset(pk):
			reservation_serializer = self.serializer_class(self.get_queryset(pk))
			return Response(reservation_serializer.data, status = status.HTTP_200_OK)
		return Response({'error': 'No existe una Reservación con estos datos'}, status = status.HTTP_400_BAD_REQUEST)

	def put(self, request, pk=None):
		if self.get_queryset(pk):
			reservation_serializer = self.serializer_class(self.get_queryset(pk), data = request.data)
			if reservation_serializer.is_valid():
				reservation_serializer.save()
				return Response(reservation_serializer.data, status = status.HTTP_200_OK)
			return Response(reservation_serializer.errors, status = status.HTTP_400_BAD_REQUEST)
