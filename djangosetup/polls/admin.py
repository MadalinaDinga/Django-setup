from django.contrib import admin

from .models import Question

admin.site.register(Question) # tell the admin that Question objects have an admin interface