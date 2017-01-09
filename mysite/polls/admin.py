from django.contrib import admin

# Register your models here.

from django.contrib import admin

from .models import Question,Choice


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3
    
    
class QuestionAdmin(admin.ModelAdmin):
	#list_display = ('question_text', 'pub_date', 'was_published_recently')
    fieldsets = [
    (None, {'fields': ['question_text']}),
    ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    search_fields = ['question_text']

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


#class QuestionAdmin(admin.ModelAdmin):
#    fieldsets = [
#    (None, {'fields': ['question_text']}),
#    ('Date information', {'fields': ['pub_date']}),
#    ]


#class QuestionAdmin(admin.ModelAdmin):
#    fields = ['pub_date', 'question_text']

admin.site.register(Question ,QuestionAdmin)
#admin.site.register(Choice)