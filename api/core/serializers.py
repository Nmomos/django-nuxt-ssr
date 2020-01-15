from rest_framework import serializers
from .models import WaterPlants


class WaterPlantsSerializer(serializers.ModelSerializer):
    class Meta:
        model = WaterPlants
        fields = (
            "id",
            "name",
            "position",
            "picture",
            "difficulty",
            "addition_amount",
            "leaf_length",
            "water_quality",
        )
