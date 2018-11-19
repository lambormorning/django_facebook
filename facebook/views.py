from django.shortcuts import render, redirect
from facebook.models import Article
from facebook.models import Comment

# Create your views here.

def new_page(request):
    if request.method == 'POST': # 폼이 전송되었을 때만 아래 코드를 실행
        new_page = Page.objects.create(
            master=request.POST['master'],
            name=request.POST['name'],
            text=request.POST['text'],
            category=request.POST['category']
        )

        # 새 페이지 개설 완료
        return redirect('/pages/')

    return render(request, 'new_page.html')



def newsfeed(request):
    articles = Article.objects.all()
    return render(request, 'newsfeed.html', {'articles': articles})

def detail_feed(request, pk):
    article = Article.objects.get(pk=pk)

    if request.method == 'POST':
        Comment.objects.create(
            article=article,
            author=request.POST.get('nickname'),
            text=request.POST.get('reply'),
            password=request.POST.get('password')
        )
        return redirect(f'/feed/{ article.pk }')

    return render(request, 'detail_feed.html', {'feed': article})

def new_feed(request):
    if request.method == 'POST': # 폼이 전송되었을 때만 아래 코드를 실행
        new_article = Article.objects.create(
            author=request.POST['author'],
            title=request.POST['title'],
            text=request.POST['content'] + "추신:감사합니다",
            password=request.POST['password']
        )
    return render(request, 'new_feed.html')


def remove_feed(request, pk):
    article = Article.objects.get(pk=pk)

    if request.method == 'POST':
        if request.POST['password'] == article.password:
            article.delete()
            return redirect('/')
        else:
            return redirect('/error.html')

    return render(request, 'remove_feed.html', {'feed':article})

def edit_feed(request, pk):
    article = Article.objects.get(pk=pk)

    if request.method == 'POST':
        if request.POST['password'] == article.password:
            article.author = request.POST['author']
            article.title = request.POST['title']
            article.text = request.POST['content']
            article.save()
            return redirect(f'/feed/{article.pk}')

    return render(request, 'edit_feed.html', {'feed':article})


def play(request):
    return render(request, 'play.html')


count = 0
def play2(request):
    name = '이상현'
    age = 20
    result = 7
    global count
    count = count + 1

    if count == 7:
        status = ''

    if age > 19:
        status = '성인'
    else :
        status = '청소년'

    diary = ['오늘은 날씨가 맑았다. -4월', '비가 온다.','이게뭐냐']

    return render(request, 'play2.html',{ 'name':name, 'cnt':count, 'age':status, 'diary':diary, 'result':result})

def profile(request):
    return render(request, 'profile.html')

def week3(request):
    num1 = 22
    multiple = 7
    if num1 % multiple is 0 :
        result = (str(num1)+'은' + str(multiple) +'의 배수입니다')
    else :
        result = (str(num1) +'은' + str(multiple) +'의 배수가 아닙니다')

    return render(request, 'week3.html',{'result':result})

