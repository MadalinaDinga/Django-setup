from django.contrib import admin
from django.urls import include, path

# To get from a URL to a view, Django uses what are known as ‘URLconfs’.
from polls import views

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('polls/<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('polls/<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('polls/<int:question_id>/vote/', views.vote, name='vote'),
    path('polls/', include('polls.urls')),  # allow referencing other URLconfs
    path('admin/', admin.site.urls),
]
