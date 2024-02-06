from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import NewsForm
from django.contrib.auth.decorators import user_passes_test

from django.shortcuts import render, get_object_or_404
from .models import News, Comment
from .forms import CommentForm


def news(request):
    news_list = News.objects.all()
    return render(request, "news.html", {"news_list": news_list, "user": request.user})


def is_admin(user):
    return user.is_authenticated and user.is_staff


@user_passes_test(is_admin)
def add_news(request):
    if request.method == "POST":
        form = NewsForm(request.POST)
        if form.is_valid():
            news = form.save(commit=False)
            news.author = request.user
            news.save()
            messages.success(request, "News added successfully!")
            return redirect("news")

    else:
        form = NewsForm()

    return render(request, "add_news.html", {"form": form})


def add_comment(request, news_id):
    news_item = News.objects.get(id=news_id)

    if request.method == "POST":
        comment_text = request.POST.get("comment_text")
        user = request.user
        if comment_text:
            comment = Comment.objects.create(
                news=news_item, text=comment_text, user=user
            )

            return redirect("view_comments", news_id=news_item.id)

    return render(request, "news.html", {"news_item": news_item, "user": request.user})


def view_comments(request, news_id):
    news_item = News.objects.get(id=news_id)
    comments = Comment.objects.filter(news=news_item)
    if request.method == "POST":
        comment_id = request.POST.get("comment_id")
        action = request.POST.get("action")

        if action == "edit":
            comment = get_object_or_404(Comment, id=comment_id, user=request.user)
            form = CommentForm(request.POST, instance=comment)
            if form.is_valid():
                form.save()
        elif action == "delete":
            comment = get_object_or_404(Comment, id=comment_id, user=request.user)
            comment.delete()

    form = CommentForm()

    return render(
        request,
        "view_comments.html",
        {"news_item": news_item, "comments": comments, "form": form},
    )
