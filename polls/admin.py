from django.contrib import admin

# Register your models here.

from .models import Question, Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    # 写法一:仅用作排序
    # fields = ['pub_date', 'question_text']

    # 写法二:表单分字段集
    fieldsets = [
        ('Date information', {'fields':['pub_date'], 'classes':['collapse']}),
        ('text information', {'fields':['question_text']}),
    ]
    # 关联了3个空的choice,但每次新增后,总会有3个空的choice出现
    inlines = [ChoiceInline]
    list_filter = ['pub_date']
    search_fields = ['question_text']
    list_display = ('question_text', 'pub_date', 'was_published_recently')

admin.site.register(Question, QuestionAdmin)
# admin.site.register(Choice)