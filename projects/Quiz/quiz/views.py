from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Quiz
from .serializers import QuizSerializer
import random


@api_view(['GET'])
def helloAPI(request):
    return Response('Hello world!')


@api_view(['GET'])
def quiz_list(request):
    totalQuizs = Quiz.objects.all()
    serializer = QuizSerializer(totalQuizs, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def quiz_detail(request, id):
    quiz = Quiz.objects.all()[id]
    serializer = QuizSerializer(quiz)
    return Response(serializer.data)



@api_view(['GET'])
def randomQuiz(request, id):
    totalQuizs = Quiz.objects.all()
    randomQuizs = random.sample(list(totalQuizs), id)
    serializer = QuizSerializer(randomQuizs, many=True)
    return Response(serializer.data)
