from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .serializers import ItemSerializer
from .models import Item 
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authentication import BasicAuthentication
from rest_framework import viewsets
from rest_framework import mixins

# Create your views here.

# @api_view(['GET'])
# def index(request):
# 	items = Item.objects.all()
# 	serializer = ItemSerializer(items, many=True)
# 	return Response(serializer.data)

class ItemViewset(viewsets.GenericViewSet,mixins.CreateModelMixin, mixins.ListModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, mixins.RetrieveModelMixin):
	serializer_class = ItemSerializer
	queryset = Item.objects.all()