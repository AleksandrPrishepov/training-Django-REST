from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics

from rest_framework.generics import ListCreateAPIView



from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *
from .serialisers import WomenSerializer



class WomenAPIView(generics.ListCreateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer

class WomenAPIViewUp(generics.RetrieveUpdateDestroyAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer


    # def get(self, request):
    #     lst = Women.objects.all()
    #     return Response({'posts': WomenSerializer(lst, many=True).data})
    #
    # def post(self, request):
    #     serializer = WomenSerializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response({'pots': serializer.data})
    #
    # def put(self, request, *args, **kwargs):
    #     pk = kwargs.get("pk", None)
    #     if not pk:
    #         return Response({"errors":"Not pk"})
    #     try:
    #         instance = Women.objects.get(pk=pk)
    #     except:
    #         return Response({"errors": "Not pk"})
    #     serializer = WomenSerializer(data=request.data, instance=instance)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response({'pots': serializer.data})

    # def delete(self, request, *args, **kwargs):
    #     pk = kwargs['pk']
    #     if pk == None:
    #         return Response({"errors": "Not pk"})
    #     try:
    #         d = Women.objects.get(pk=pk).delete()
    #     except:
    #         return Response({"errors": "Not pk"})
    #     return Response({"pots":"deleted post"+str(pk)})







