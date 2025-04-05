from rest_framework import serializers

from app.models import CustomUser, Question, Choice


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(source='choice_set', many=True, required=False, allow_null=True)
    class Meta:
        model = Question
        fields = '__all__'
        read_only_fields = ["choices"]