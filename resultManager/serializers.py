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

    def create(self, validated_data):
        scores_data = validated_data.pop('scores')
        student = Student.objects.create(**validated_data)
        for score_data in scores_data:
            Score.objects.create(student=student, **score_data)
        return student
