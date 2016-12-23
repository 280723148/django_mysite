from django.contrib import admin

# Register your models here.

from django.contrib import admin

from .models import Question,Choice

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
    (None, {'fields': ['question_text']}),
    ('Date information', {'fields': ['pub_date']}),
    ]


#class QuestionAdmin(admin.ModelAdmin):
#    fields = ['pub_date', 'question_text']

admin.site.register(Question ,QuestionAdmin)
admin.site.register(Choice)