from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import User
from sclone.serializer import UserSerializer,QuestionModelSerializer,AnswerModelSerializer
from rest_framework.response import Response
from sclone.models import Questions,Answers
from rest_framework.decorators import action

# Create your views here.

class UserView(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

class QuestionsModelViewsetView(ModelViewSet):

    serializer_class = QuestionModelSerializer
    queryset = Questions.objects.all()

    @action(methods=["POST"], detail=True)
    def add_answer(self, request, *args, **kwargs):
        #  localhost:8000/api/v2/products/1/add_review/
        id=kwargs.get("pk")
        question=Questions.objects.get(id=id)
        Answers.objects.create(question=question,answer=request.data.get("answer"),
                               user=request.user,
                               upvote=request.data.get('upvote'))
        return Response(data="created")

class AnswerModelViewsetView(ModelViewSet):
    serializer_class = AnswerModelSerializer
    queryset = Answers.objects.all()
    def list(self, request, *args, **kwargs):
        all_answers=Answers.objects.all()
        if 'user' in request.query_params:
            all_answers=all_answers.filter(user=request.query_params.get("user"))
        serializer = AnswerModelSerializer(all_answers, many=True)
        return Response(data=serializer.data)