from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import ClockGmt


class ClockGmtSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClockGmt
        fields = ('id','text', 'gmt')
