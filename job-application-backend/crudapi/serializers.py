
from django.db.models import fields
from rest_framework import serializers
from .models import Userjob
  
class UserjobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Userjob
        fields = ('email', 'jobId')