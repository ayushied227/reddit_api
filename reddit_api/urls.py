from django.urls import path
from reddit_api import views

urlpatterns = [
    path('register', views.Register.as_view(), name='register'),
    path('login', views.Login.as_view(), name="login"),
    path('logout', views.Logout.as_view(), name="logout"),
    path('get-current-user', views.GetCurrentUser.as_view())
]