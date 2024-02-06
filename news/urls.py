from django.urls import path, include
from .views import news, add_news, add_comment, view_comments

urlpatterns = [
    path(" ", news, name="news"),
    path("add_news/", add_news, name="add_news"),
    path("add_comment/", add_comment, name="add_comment"),
    path("news/<int:news_id>/", add_comment, name="add_comment"),
    path("view_comments/", view_comments, name="view_comments"),
    path("news/view_comments/<int:news_id>/", view_comments, name="view_comments"),
]
