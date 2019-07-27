from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, RetrieveUpdateAPIView, DestroyAPIView
from classes.models import *
from .serializer import *
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

# Create your views here.
class ClassListView(ListAPIView):
    queryset = Classroom.objects.all()
    serializer_class = ClassListSerializer

class ClassDetailView(RetrieveAPIView):
    queryset = Classroom.objects.all()
    serializer_class = ClassDetailSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'classroom_id'

class ClassCreateView(CreateAPIView):
    serializer_class = ClassCreateSerializer
    def perform_create(self, serializer):
        serializer.save(teacher=self.request.user)

class ClassUpdateView(RetrieveUpdateAPIView):
    queryset = Classroom.objects.all()
    serializer_class = ClassCreateSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'classroom_id'

class ClassDeleteView(DestroyAPIView):
    queryset = Classroom.objects.all()
    serializer_class = ClassListSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'classroom_id'

class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer

# class UserLoginAPIView(APIView):
#     serializer_class = UserLoginSerializer

    # def post(self, request):
    #     my_data = request.data
    #     serializer = UserLoginSerializer(data=my_data)
    #     if serializer.is_valid(raise_exception=True):
    #         valid_data = serializer.data
    #         return Response(valid_data, status=HTTP_200_OK)
    #     return Response(serializer.errors, HTTP_400_BAD_REQUEST)