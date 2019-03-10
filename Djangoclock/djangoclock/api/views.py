from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import ClockGmtSerializer
from .models import ClockGmt


class ClockGmtViewSet(viewsets.ModelViewSet):

    queryset = ClockGmt.objects.all()
    serializer_class = ClockGmtSerializer
