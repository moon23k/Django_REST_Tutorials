from django.contrib import admin
from .models import Quiz

#@admin.register(Quiz) 데코레이터를 사용할 때는 데코레이터의 꾸밈을 받은 클래스가 따라와야한다
admin.site.register(Quiz)
