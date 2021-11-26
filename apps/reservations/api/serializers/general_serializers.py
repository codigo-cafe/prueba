from apps.reservations.models import Rooms
from apps.clients.models import Client
from rest_framework import serializers

class RoomsSerializer(serializers.ModelSerializer):

	class Meta:
		model = Rooms
		exclude = ('sw','created_date','modified_date','delete_date')

class ClientSerializer(serializers.ModelSerializer):

	class Meta:
		model = Client
		exclude = ('username','password','last_login','is_superuser','is_staff','groups','user_permissions')