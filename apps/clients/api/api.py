from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from apps.clients.models import Client
from apps.clients.api.serializers import ClientSerializer,ClientListSerializer

@api_view(['GET', 'POST'])
def client_api_view(request):
	# List
	if request.method == 'GET':
		# queryset
		clients = Client.objects.all()
		clients_serializer = ClientListSerializer(clients, many = True)
		return Response(clients_serializer.data, status = status.HTTP_200_OK)
	#create
	elif request.method == 'POST':
		client_serializer = ClientSerializer(data = request.data)
		#validation
		if client_serializer.is_valid():
			client_serializer.save()
			return Response({'message': 'Cliente creado correctamente'}, status = status.HTTP_201_CREATED)

		return Response(client_serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def client_detail_api_view(request, pk=None):
	#query
	client = Client.objects.filter(id = pk).first()
	#validation
	if client:
		#retrieve
		if request.method =='GET':
			client_serializer = ClientSerializer(client)
			return Response(client_serializer.data, status = status.HTTP_200_OK)
		#update
		elif request.method == 'PUT':
			client_serializer = ClientSerializer(client, data = request.data)
			if client_serializer.is_valid():
				client_serializer.save()
				return Response({'message': 'Usuario Actualizado correctamente!'}, status = status.HTTP_200_OK)

			return Response(client_serializer.errors, status = status.HTTP_400_BAD_REQUEST)
		#delete
		elif request.method == 'DELETE':
			client.delete()
			return Response({'message': 'Usuario Eliminado correctamente!'}, status = status.HTTP_200_OK)

	return Response({'message': 'No se ha encontrado un cliente con estos datos'}, status = status.HTTP_400_BAD_REQUEST)