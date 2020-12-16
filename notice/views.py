from django.shortcuts import render, redirect

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from account.forms import RegisterForm
from notice.models import Note


# 페이징 하기 전에 리스트
# def notice_list(request):
#     articles = Note.objects.all().order_by('-pk')
#
#     return render(request, 'notice/notice_list.html', {'articles': articles})


def notice_list(request):
    PAGE_ROW_COUNT = 5
    PAGE_DISPLAY_COUNT = 2

    total_list = Note.objects.all().order_by('-pk')

    paginator = Paginator(total_list, PAGE_ROW_COUNT)
    pageNum = request.GET.get('pageNum')

    totalPageCount = paginator.num_pages  # 전체 페이지 갯수

    try:
        member_list = paginator.page(pageNum)
    except PageNotAnInteger:
        member_list = paginator.page(1)
        pageNum = 1
    except EmptyPage:
        member_list = paginator.page(paginator.num_pages)
        pageNum = paginator.num_pages

    pageNum = int(pageNum)

    startPageNum = 1 + ((pageNum - 1) / PAGE_DISPLAY_COUNT) * PAGE_DISPLAY_COUNT
    endPageNum = startPageNum + PAGE_DISPLAY_COUNT - 1
    if totalPageCount < endPageNum:
        endPageNum = totalPageCount

    bottomPages = range(int(startPageNum), int(endPageNum + 1))

    return render(request, 'notice/notice_list.html',
                  {
                      'member_list': member_list,
                      'pageNum': pageNum,
                      'bottomPages': bottomPages,
                      'totalPageCount': totalPageCount,
                      'startPageNum': startPageNum,
                      'endPageNum': endPageNum
                  }
                  )


def notice_detail(request, pk):
    article = Note.objects.get(pk=pk)

    return render(request, 'notice/notice_detail.html', {'feed': article})


def notice_create(request):
    if request.method == 'POST':
        if request.POST['author'] != '' and request.POST['title'] != '' and request.POST['content'] != '' and \
                request.POST['password'] != '':
            new_article = Note.objects.create(
                author=request.POST['author'],
                title=request.POST['title'],
                text=request.POST['content'],
                password=request.POST['password']
            )

            return redirect(f'/notice/feed/{new_article.pk}')

    return render(request, 'notice/notice_create.html')


def notice_update(request, pk):
    article = Note.objects.get(pk=pk)

    if request.method == 'POST':
        if request.POST['password'] == article.password:
            article.author = request.POST['author']
            article.title = request.POST['title']
            article.text = request.POST['content']
            article.save()

            return redirect('/notice/')
        else:
            return render(request, 'notice/notice_update.html', {'error': '** 비밀번호가 같지 않습니다.', 'feed': article})

    return render(request, 'notice/notice_update.html', {'feed': article})


def notice_delete(request, pk):
    article = Note.objects.get(pk=pk)

    if request.method == 'POST':
        if request.POST['password'] == article.password:
            article.delete()
            return redirect('/notice/')

        else:
            return render(request, 'notice/notice_delete.html', {'error': '** 비밀번호가 같지 않습니다.', 'feed': article})

    return render(request, 'notice/notice_delete.html', {'feed': article})
