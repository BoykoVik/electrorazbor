from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Article
from coreapp.models import Contacts

# Create your views here.
def articledetail(request, slug):
    article = Article.objects.filter(slug=slug).first()
    return render(request, 'articlesapp/article_detail.html', {
        'title': article.title,
        'description': article.description,
        'all_blocks': article.get_all_blocks_sorted() if article else [],
        'article': article,
        'contacts': Contacts.objects.all(),
    })

def blog_list(request):
    articles = Article.objects.all()
    if 'page' in request.GET:
        page_num = request.GET['page']
    else:
        page_num = 1
    paginator = Paginator(articles, 12)
    page = paginator.get_page(page_num)
    return render(request, 'articlesapp/blog.html', {
        'title': '',
        'description': '',
        'articles': page.object_list,
        'page': page,
    })