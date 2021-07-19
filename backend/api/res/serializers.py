from rest_framework import serializers
from .models import Res


class ResSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'title',
            'description',
        )
        model = Res