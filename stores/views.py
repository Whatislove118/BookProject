import generics as generics
from django.contrib.auth import get_user_model
from django.shortcuts import render
from rest_framework import generics, permissions
# Create your views here.
from rest_framework.parsers import MultiPartParser, JSONParser

from stores.mixins import QuerysetSerializerMixin
from stores.models import Pizzeria
from stores.serializers import PizzeriaListSerializer, PizzeriaDetailSerializer, UserSerializer


## получить список
class PizzeriaListAPIView(QuerysetSerializerMixin, generics.ListAPIView):
    serializer_class = PizzeriaListSerializer

class PizzeriaDetailAPIView(QuerysetSerializerMixin, generics.RetrieveAPIView):
    lookup_field = 'id'  # обязательное поле. Указывает, по какому полю мы будем делать запрос к модели. Также используется в URL

class PizzeriaCreateAPIView(QuerysetSerializerMixin, generics.CreateAPIView):
    parser = [MultiPartParser]  # джанго рест поставляется с 4 парсерами: JSONParser, FormParser, MultiPartParser, FileUploadParser
    pass

class PizzeriaRetrieveUpdateAPIView(QuerysetSerializerMixin, generics.RetrieveUpdateAPIView):
    lookup_field = 'id'

class PizzeriaDestroyAPIView(generics.DestroyAPIView):
    lookup_field = 'id'
    queryset = Pizzeria.objects.all()
    ## сериализатор не нужен


class UserCreateView(generics.CreateAPIView):
    model = get_user_model()
    parser_classes = [JSONParser]
    permission_classes = [permissions.AllowAny]
    serializer_class = UserSerializer