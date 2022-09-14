from django.urls import path
from onne_envios.views import index

urlpatterns = [path('', index)
]
