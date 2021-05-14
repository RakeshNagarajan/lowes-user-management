from .serializers import UserSerializer
from .models import user as User
from rest_framework import viewsets

class usermanagementViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    #filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name']