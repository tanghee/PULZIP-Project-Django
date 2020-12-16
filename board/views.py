from django.shortcuts import render, redirect

from account.forms import RegisterForm
from board.models import Post


def board_list(request):
    articles = Post.objects.all().order_by('-pk')

    return render(request, 'board/board_list.html', {'articles': articles})


def board_detail(request, pk):
    article = Post.objects.get(pk=pk)

    return render(request, 'board/board_detail.html', {'feed': article})


def board_create(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            if request.POST['author'] != '' and request.POST['title'] != '' and request.POST['content'] != '' and \
                    request.POST['password'] != '':

                new_article = Post.objects.create(
                    author=request.POST['author'],
                    title=request.POST['title'],
                    text=request.POST['content'],
                    password=request.POST['password']
                )

                return redirect(f'/board/feed/{new_article.pk}')
        else:
            return render(request, 'board/board_create.html', {'error': '로그인을 하셔야 작성하실 수 있습니다.'})

    return render(request, 'board/board_create.html')


def board_update(request, pk):
    article = Post.objects.get(pk=pk)

    if request.method == 'POST':
        if request.user.is_authenticated:
            # if request.user.is_active == article.author:
            if request.POST['password'] == article.password:
                article.author = request.POST['author']
                article.title = request.POST['title']
                article.text = request.POST['content']
                article.save()

                return redirect('/board/')
            else:
                return render(request, 'board/board_update.html', {'error': '비밀번호가 같지 않습니다.', 'feed': article})
            # else:
            #     return render(request, 'board/board_update.html', {'error': '수정할 수 있는 권한이 없습니다.', 'feed': article})
        else:
            return render(request, 'board/board_update.html', {'error': '로그인을 하셔야 작성하실 수 있습니다.', 'feed': article})
    return render(request, 'board/board_update.html', {'feed': article})


def board_delete(request, pk):
    article = Post.objects.get(pk=pk)

    if request.method == 'POST':
        if request.user.is_authenticated:
            if request.POST['password'] == article.password:
                article.delete()
                return redirect('/board/')

            else:
                return render(request, 'board/board_delete.html', {'error': '비밀번호가 같지 않습니다.', 'feed': article})
        else:
            return render(request, 'board/board_delete.html', {'error': '로그인을 하셔야 작성하실 수 있습니다.', 'feed': article})

    return render(request, 'board/board_delete.html', {'feed': article})
