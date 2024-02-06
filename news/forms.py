# forms.py
from django import forms
from .models import News, Comment


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ["title", "content"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["title"].widget.attrs.update({"class": "form-control"})
        self.fields["content"].widget.attrs.update(
            {"class": "form-control", "rows": "4"}
        )


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["text"]
