
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views


urlpatterns = [
    path('', views.tweet_list, name="tweet_list"),
    path('create/', views.tweet_create, name="tweet_create"),

    # optional detail view for a single tweet (uses same view function)
    path('<int:tweet_id>/', views.tweet_list, name="tweet_form"),

    path('<int:tweet_id>/delete/', views.tweet_delete, name="tweet_delete"),
    path('<int:tweet_id>/edit/', views.tweet_edit, name="tweet_edit"),
    path('register/', views.register, name="register"),

]