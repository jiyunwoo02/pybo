from django.contrib import admin
from .models import Question

# 1. 모델 등록
# admin.site.register(Question)

# 2. Question 모델에 세부 기능을 추가할 수 있는 QuestionAdmin 클래스를 생성
# + 제목 검색을 위해 search_fields 속성에 'subject'를 추가
# --> 검색기능이 추가된 화면
class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject']

admin.site.register(Question, QuestionAdmin)
