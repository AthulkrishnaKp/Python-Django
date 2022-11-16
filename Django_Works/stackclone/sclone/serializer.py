

from rest_framework import serializers
from sclone.models import Questions,Answers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["first_name","last_name","username","email","password"]

    def create(self,validated_data):
        return User.objects.create_user(**validated_data)

class QuestionModelSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    class Meta:
        model = Questions
        fields = "__all__"


class AnswerModelSerializer(serializers.ModelSerializer):
    posted_date = serializers.CharField(read_only=True)
    class Meta:
        model = Answers
        fields = "__all__"