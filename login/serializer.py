
from rest_framework import serializers
from .models import *


class ScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testscore
        fields = ['username', 'semester', 'score', 'testkey']


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questionbank
        fields = ['semester', 'question', 'optionA',
                  'optionB', 'optionC', 'optionD', 'answer', 'testkey', 'teacher_username', 'quizname']
