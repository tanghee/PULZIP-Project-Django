from django.shortcuts import render

from board.models import Post
from notice.models import Note
from main.models import Slide


def main_link(request):
    articles = Post.objects.all().order_by('-pk')[:5]
    notices = Note.objects.all().order_by('-pk')[:5]
    slide = Slide.objects.all()

    return render(request, 'main/index.html', {'articles': articles, 'notices': notices, 'slide': slide})
