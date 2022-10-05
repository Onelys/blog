from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='index'),
    path('proclamacion/', proclamacion, name='proclamacion'),
    path('enceñanza/', enceñanza, name='enceñanza'),
    path('servicio/', servicio, name='servicio'),
    path('comunion/', comunion, name='comunion'),
    path('alavanza/', alavanza, name='alavanza'),
    path('recursos/', recursos, name='recursos'),
    path('<slug:slug>/', detallePost, name='detalle_post'), 
    
]
