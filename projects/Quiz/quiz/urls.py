from django.urls import path, include
from .views import *


urlpatterns = [
    path('', quiz_list),
    path('<int:id>', quiz_detail),
    path('hello/', helloAPI),
    path('random/<int:id>', randomQuiz),
]