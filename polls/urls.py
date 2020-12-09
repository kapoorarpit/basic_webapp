from django.urls import path

from . import views

from django.urls import path

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /5/
    path('spe/<int:question_id>/', views.detail, name='detail'),
    # ex: /5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]