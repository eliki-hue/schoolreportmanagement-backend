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
        fields = ['id', 'name', 'scores', 'email']

    def create(self, validated_data):
        scores_data = validated_data.pop('scores')
        student = Student.objects.create(**validated_data)
        for score_data in scores_data:
            Score.objects.create(student=student, **score_data)
        return student
    
    def update(self, instance, validated_data):
        scores_data = validated_data.pop('scores')
        scores = instance.scores.all()
        scores = list(scores)
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        for score_data in scores_data:
            if scores:
                score = scores.pop(0)
                score.subject = score_data.get('subject', score.subject)
                score.score = score_data.get('score', score.score)
                score.save()
            else:
                Score.objects.create(student=instance, **score_data)
        return instance
