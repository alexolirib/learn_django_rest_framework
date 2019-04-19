from rest_framework.parsers import JSONParser

from .models import Car
from .serializers import CarSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import permissions, status
from learn_django_rest_framework.permissions import IsOwnerOrReadOnly


class CarListAndAdd(APIView):

    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly, IsAuthenticated)

    def get(self, request, *args, **kwargs):
        listaCar = Car.objects.all()
        serializer = CarSerializer(listaCar, many=True)
        return Response(serializer.data)


    def post(self, request, *args, **kwargs):
        data = JSONParser().parse(request)
        serializer = CarSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CarDetail(APIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly, IsAuthenticated)

    def get(self, request, *args, **kwargs):
        try:
            car = Car.objects.get(idCarro=kwargs['id_carro'])
            serializer = CarSerializer(car)
            return Response(serializer.data)

        except:
            return Response(data='car not found', status=status.HTTP_404_NOT_FOUND)



