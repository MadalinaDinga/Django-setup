from django.contrib import admin

from .models import Report, Comment


class ChoiceInline(admin.TabularInline):
    model = Comment
    extra = 1


class ReportAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    list_display = ('report_text', 'pub_date', 'report_likes', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['report_text']


admin.site.register(Report, ReportAdmin)
