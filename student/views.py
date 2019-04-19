from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework import generics

from rest_framework import mixins
from rest_framework import permissions

from rest_framework.views import APIView

from student.models import Student
from django.contrib.auth.models import User
from student.serializers import StudentSerializer, StudentInfoImpSerializer
from rest_framework.permissions import IsAuthenticated
from learn_django_rest_framework.permissions import IsOwnerOrReadOnly
#antes da autenticação
# from student.serializers import StudentSerializer
#https://www.django-rest-framework.org/api-guide/renderers/


# class StudentList(mixins.ListModelMixin,
#                   mixins.CreateModelMixin,
#                   generics.GenericAPIView):
#     queryset = User.objects.all()
#     serializer_class = StudentSerializer
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    #permission_classes = (permissions.IsAuthenticated,)

    # def perform_create(self, serializer):
    #     serializer.save(owner=self.request.user)
    #
    # def get(self, request, *args, **kwargs):
    #     return self.list(request, *args, **kwargs)
    #
    # def post(self, request, *args, **kwargs):
    #     return self.create(request, *args, **kwargs)


class StudentList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


# class StudentList(APIView):
#
#     def get(self, request, format =None):
#         students = Student.objects.all()
#         serializer = StudentSerializer(students, many=True)
#         return Response(serializer.data)
#
#     def post(self, request, format=None):
#         data = JSONParser().parse(request)
#         serializer = StudentSerializer(data = data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET', 'POST'])
# def student_list(request, format=None):
#
#     if request.method == 'GET':
#         students = Student.objects.all()
#         serializer = StudentSerializer(students, many=True)
#         return Response(serializer.data)
#
#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = StudentSerializer(data = data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StudentDetail(APIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly, IsAuthenticated)

    def get(self, request, *args, **kwargs):
        try:
            student = Student.objects.get(id=kwargs['pk'])
            serializer = StudentInfoImpSerializer(student)
            return Response(serializer.data)

        except:
            return Response(data="Student not found",status=status.HTTP_404_NOT_FOUND)


class StudentCustomized(APIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly, IsAuthenticated)

    def get(self, request, *args, **kwargs):
        student = Student(name="Samia Ribeiro", age=35, discount=False)
        serializer = StudentInfoImpSerializer(student)
        return Response(serializer.data)
