from django.urls import path
from . import views

urlpatterns = [
    path('', views.principal, name='principal'),
    path('vuelos/', views.VueloListView.as_view(), name='vuelos'),
    path('vuelos/<int:pk>', views.VueloDetailView.as_view(), name='vuelo-detail'),
    path('aviones/', views.AvionListView.as_view(), name='aviones'),
    path('aviones/<int:pk>', views.AvionDetailView.as_view(), name='avion-detail'),
    path('aviones/create', views.AvionCreate.as_view(), name='avion-create'),
    path('aviones/<int:pk>/update/', views.AvionUpdate.as_view(), name='avion-update'),
    path('aviones/<int:pk>/delete/', views.AvionDelete.as_view(), name='avion-delete'),
    path('empleados/', views.EmpleadoListView.as_view(), name='empleados'),
    path('empleados/<int:pk>', views.EmpleadoDetailView.as_view(), name='empleado-detail'),
    path('empleados/create', views.EmpleadoCreate.as_view(), name='empleado-create'),
    path('empleados/<int:pk>/update/', views.EmpleadoUpdate.as_view(), name='empleado-update'),
    path('empleados/<int:pk>/delete/', views.EmpleadoDelete.as_view(), name='empleado-delete'),

]