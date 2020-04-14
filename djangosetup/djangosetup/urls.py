from django.contrib import admin
from django.urls import include, path

# To get from a URL to a view, Django uses what are known as ‘URLconfs’.
from polls import views

urlpatterns = [
    path('polls/', include('polls.urls')),  # allow referencing other URLconfs
    path('admin/', admin.site.urls),
]
