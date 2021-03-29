from django.urls import path, include
from rest_framework.routers import DefaultRouter

from restoration.apps.furniture.views import LegsViewSet, LegsView, TablesViewSet, FeetViewSet, FeetView, TableView

router = DefaultRouter()
router.register(r'legs-list', LegsViewSet, basename='legs-list')
router.register(r'feet-list', FeetViewSet, basename='feet-list')
router.register(r'tables-list', TablesViewSet, basename='tables-list')

urlpatterns = [
    path('', include(router.urls)),
    path('leg-view/', LegsView.as_view(), name='leg_view'),
    path('leg-view/<int:pk>/', LegsView.as_view(), name='leg'),
    path('feet-view/', FeetView.as_view(), name='feet_view'),
    path('feet-view/<int:pk>/', FeetView.as_view(), name='feet'),
    path('table-view/', TableView.as_view(), name='table_view'),
    path('table-view/<int:pk>/', TableView.as_view(), name='table'),
]
