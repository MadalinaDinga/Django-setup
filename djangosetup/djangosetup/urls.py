from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('polls/', include('polls.urls')),  # allow referencing other URLconfs
    path('admin/', admin.site.urls),
]