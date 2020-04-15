from django.urls import path

from . import views

app_name = 'reports'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:report_id>/like/', views.like, name='like'),
    path('<int:report_id>/comment/', views.comment, name='comment'),
]
