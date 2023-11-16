from django.urls import path
from . import views

urlpatterns = [
    path('rolex-watches/', views.getRolexWatches, name='rolex-watches'),
    path('rolex/<str:pk>', views.getRolex, name='rolex'),
]