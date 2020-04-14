from django.contrib import admin

from .models import Question, Choice


# class ChoiceInline(admin.StackedInline):
class ChoiceInline(admin.TabularInline): # Tabular way of displaying inline related objects
    model = Choice
    extra = 3


# split the form up into fieldsets
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline] # Choice objects are edited on the Question admin page
    list_display = ('question_text', 'pub_date', 'was_published_recently') # Display individual fields instead of the default str() of each object
    list_filter = ['pub_date'] # add a “Filter” sidebar that lets people filter the change list by the pub_date field
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)