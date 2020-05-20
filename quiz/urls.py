from django.urls import path

from . import views

app_name = 'quizes'
urlpatterns = [
    path('', views.index, name = 'index'),
    # ex: /quizes/5
    path('<int:quiz_id>/', views.detail, name = 'detail'),
    path('<int:quiz_id>/answer/', views.answer, name = 'answer')
]