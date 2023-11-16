from rest_framework import serializers
from .models import Rolex

class RolexSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rolex
        fields = "__all__"

