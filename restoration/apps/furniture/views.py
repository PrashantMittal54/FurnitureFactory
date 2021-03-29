from django.shortcuts import render
from rest_framework import mixins, viewsets, filters as search_filters, status
from rest_framework.generics import GenericAPIView
from rest_framework.pagination import LimitOffsetPagination

from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from restoration.apps.furniture.serializers import LegsSerializer, FeetSerializer, TablesSerializer
from restoration.apps.furniture.models import Legs, Feet, Tables


class LegsViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    serializer_class = LegsSerializer
    filter_backends = (search_filters.SearchFilter, search_filters.OrderingFilter)
    search_fields = ['id', 'name']
    pagination_class = LimitOffsetPagination
    ordering_fields = ['id', 'name']
    permission_classes = [AllowAny]
    queryset = Legs.objects.all()


class LegsView(GenericAPIView):
    serializer_class = LegsSerializer
    permission_classes = [AllowAny]

    def get(self, request, pk):
        leg = Legs.objects.get(id=pk)
        data = self.get_serializer(leg, many=False).data
        return Response(data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        leg = Legs.objects.get(id=pk)
        serializer = self.get_serializer(leg, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        leg = Legs.objects.get(id=pk)
        leg.delete()
        return Response({"message": 'Leg deleted successfully'}, status=status.HTTP_200_OK)


class FeetViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    serializer_class = FeetSerializer
    filter_backends = (search_filters.SearchFilter, search_filters.OrderingFilter)
    search_fields = ['id', 'name']
    pagination_class = LimitOffsetPagination
    ordering_fields = ['id', 'name']
    permission_classes = [AllowAny]
    queryset = Feet.objects.all()


class FeetView(GenericAPIView):
    serializer_class = FeetSerializer
    permission_classes = [AllowAny]

    def get(self, request, pk):
        feet = Feet.objects.get(id=pk)
        data = self.get_serializer(feet, many=False).data
        return Response(data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        feet = Feet.objects.get(id=pk)
        serializer = self.get_serializer(feet, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        feet = Feet.objects.get(id=pk)
        feet.delete()
        return Response({"message": 'Feet deleted successfully'}, status=status.HTTP_200_OK)


class TablesViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    serializer_class = TablesSerializer
    filter_backends = (search_filters.SearchFilter, search_filters.OrderingFilter)
    search_fields = ['id', 'name']
    pagination_class = LimitOffsetPagination
    ordering_fields = ['id', 'name']
    permission_classes = [AllowAny]
    queryset = Tables.objects.all()


class TableView(GenericAPIView):
    serializer_class = TablesSerializer
    permission_classes = [AllowAny]

    def get(self, request, pk):
        table = Tables.objects.get(id=pk)
        data = self.get_serializer(table, many=False).data
        return Response(data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        table = Tables.objects.get(id=pk)
        serializer = self.get_serializer(table, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        table = Tables.objects.get(id=pk)
        table.delete()
        return Response({"message": 'Table deleted successfully'}, status=status.HTTP_200_OK)


def index(request):
    """View function for home page of site."""
    return render(request, 'index.html')
