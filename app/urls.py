from django.contrib import admin
from django.urls import path

from app import views

urlpatterns = [
    path('', views.QuestionsList, name='QuestionsList'),
    path('hot/', views.QuestionsHot, name='QuestionsHot'),
    path('tag/<str:tag_name>', views.TagsList, name='TagsList'),
    path('question/<int:question_id>', views.QuestionSingle, name='QuestionSingle'),
    path('login/', views.Login, name='Login'),
    path('register/', views.Register, name='Register'),
    path('ask/', views.AddQuestion, name='AddQuestion'),
    path('settings/', views.Settings, name='Settings'),

]