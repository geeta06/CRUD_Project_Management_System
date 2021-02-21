from rest_framework import serializers
from .models import Project, Task

class ProjectListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = ('id', 'name', 'description', 'duration', 'avtar')

    def create(self, validated_data):
        validated_data['name'] = validated_data.get('name')
        validated_data['description'] = validated_data.get('description')
        validated_data['duration'] = validated_data.get('duration')
        validated_data['avtar'] = validated_data.get('avtar')
        return Project.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name')
        instance.description = validated_data.get('description')
        instance.duration = validated_data.get('duration')
        instance.avtar = validated_data.get('avtar')
        instance.save()
        return instance

class TaskListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ('id', 'name', 'description', 'start_date', 'end_date', 'project')

    def create(self, validated_data):
        validated_data['name'] = validated_data.get('name')
        validated_data['description'] = validated_data.get('description')
        validated_data['start_date'] = validated_data.get('start_date')
        validated_data['end_date'] = validated_data.get('end_date')
        validated_data['project'] = validated_data.get('project')
        return Task.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name')
        instance.description = validated_data.get('description')
        instance.start_date = validated_data.get('start_date')
        instance.end_date = validated_data.get('end_date')
        instance.project = validated_data.get('project')
        instance.save()
        return instance

