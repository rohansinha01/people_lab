from .models import Character
from rest_framework import viewsets, permissions
from .serializers import CharacterSerializer

class CharacterViewSet(viewsets.ModelViewSet):
    queryset=Character.objects.all()
    serializer_class=CharacterSerializer
    permission_classes=[permissions.AllowAny]
