from django.contrib import admin
from django.urls import include, path

from djangosetup.polls import views

# To get from a URL to a view, Django uses what are known as ‘URLconfs’.

urlpatterns = [
# ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('polls/', include('polls.urls')),  # allow referencing other URLconfs
    path('admin/', admin.site.urls),
]