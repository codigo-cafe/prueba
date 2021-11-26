from rest_framework import serializers
from apps.clients.models import Client

class ClientSerializer(serializers.ModelSerializer):
	class Meta:
		model = Client
		fields = '__all__'

	def create(self, validated_data):
		client = Client(**validated_data)
		client.set_password(validated_data['password'])
		client.save()
		return client

	def update(self, instance, validated_data):
		update_client = super().update(instance, validated_data)
		update_client.set_password(validated_data['password'])
		update_client.save()
		return update_client

class ClientListSerializer(serializers.ModelSerializer):
	class Meta:
		model = Client


	def to_representation(self, instance):
		return {
			'id': instance.id,
			'username': instance.username,
			'password': instance.password,
			'ci': instance.ci,
			'name': instance.name,
			'last_name': instance.last_name,
		}