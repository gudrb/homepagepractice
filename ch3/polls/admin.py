from django.contrib import admin
from polls.models import Question, Choice
# Register your models here.
class ChoiceInline(admin.TabularInline):
    model=Choice
    extra=2
class QuestionAdmin(admin.ModelAdmin):
    fieldsets=[
        (None,{'fields':['question_text']}),
        ('Date Information',{'fields':['pub_date'],'classes':['collapse']}),
    ]
    inlines=[ChoiceInline]
    list_display=('question_text','pub_date') #레코드 리스트 항목
    list_filter=['pub_date'] #필터 사이드바 추가
    search_fields=['question_text']# 검색 박스 추가
admin.site.register(Question,QuestionAdmin)
admin.site.register(Choice)