  
from rest_framework import serializers
from profiles.models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'studentId', 'name']

    def create(self, validated_data):
        
        return Profile.objects.create(**validated_data)

    def update(self, instance, validated_data):
        
        instance.studentId = validated_data.get('id', instance.studentId)
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance
