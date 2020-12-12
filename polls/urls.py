from django.urls import path

from . import views

from django.urls import path

app_name= 'polls'
urlpatterns = [
    path('', views.index.as_view(), name='index'),
    path('<int:pk>/', views.detail.as_view(), name='detail'),
    path('<int:pk>/results/', views.results.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]