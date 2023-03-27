from rest_framework import serializers
from .models import Student, Score

class ScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Score
        fields = ['subject', 'score']

class StudentSerializer(serializers.ModelSerializer):
    scores = ScoreSerializer(many=True)

    class Meta:
        model = Student
        fields = ['id', 'name', 'scores']