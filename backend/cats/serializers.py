from rest_framework import serializers

from .models import Cat, Mission, Target
from .services import validate_breed_func


class CatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cat
        fields = "__all__"
    
    def validate_breed(self, value):
        if not validate_breed_func(value):
            raise serializers.ValidationError(f"The breed doesn`t exist")
        return value
    

class TargetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Target
        fields = ['id', 'name', 'country', 'notes', 'is_completed']


class MissionSerializer(serializers.ModelSerializer):
    targets = TargetSerializer(many=True)

    class Meta:
        model = Mission
        fields = ["id", "cat", "is_completed"]
    
    def validate_targets(self, value):
        if not (1 <= len(value) <= 3):
            raise serializers.ValidationError("The mission must be in the range of 1 to 3")
        return value
    
    def validate_cat(self, value):
        if value:
            active_mission = Mission.objects.filter(cat=value, is_complete=False).exists()
            if active_mission:
                raise serializers.ValidationError("This cat has already an active mission")
        return value

    def create(self, validated_data):
        targets_data = validated_data.pop('targets')
        mission = Mission.objects.create(**validated_data)
        for target_data in targets_data:
            Target.objects.create(mission=mission, **target_data)
        return mission
    
    def update(self, instance, validated_data):
        return super().update(instance, validated_data)
