from rest_framework import serializers
from apps.reservations.models import Reservation
from apps.reservations.api.serializers.general_serializers import RoomsSerializer, ClientSerializer

class ReservationSerializer(serializers.ModelSerializer):

	class Meta:
		model = Reservation
		exclude = ('sw','created_date','modified_date','delete_date')

	def to_representation(self, instance):
		return {
			'id': instance.id,
			'status': instance.status,
			'date_start': instance.date_start,
			'date_end': instance.date_end,
			'mount': instance.mount,
			'payment_method': instance.payment_method,
			'client': instance.client.ci,
			'room': instance.room.number,
		}