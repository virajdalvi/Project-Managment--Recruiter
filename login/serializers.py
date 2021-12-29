
from rest_framework import serializers
from . models import *


class ReactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testscore
        fields = ['username', 'semester', 'score']
