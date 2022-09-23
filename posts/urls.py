from django.urls import path
from posts import views

urlpatterns = [
    path('create-question', views.CreateQuestion.as_view(), name="create-question"),
    path('questions/<pk>', views.GetQuestion.as_view()),
    path('create-answer/<pk>', views.CreateAnswer.as_view()),
    path('get-answers/<pk>', views.GetAnswers.as_view()),
    path('upvote/<model>/<pk>', views.Upvote.as_view()),
    path('downvote/<model>/<pk>', views.Downvote.as_view()),
]