from django.urls import path
from .views import PersonAPIView

urlpatterns = [
    path('people/', PersonAPIView.as_view(), name='person-api'),
]