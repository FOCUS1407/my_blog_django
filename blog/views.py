from unicodedata import category
from django import http
from django.shortcuts import render
from .models import Article, Category
from django.core.paginator import Paginator

def home(request):
    list_articles=Article.objects.all().order_by('-created_at')
    paginator = Paginator(list_articles, 4) # Affiche 4 articles par page
    
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context= {"liste_articles":page_obj}
    return render(request,"index.html",context) 

### Détaille sur un Article
def detail(request,id_article):
    article=Article.objects.get(id=id_article)
    category=article.category
    article_en_relation=Article.objects.filter(category=category).exclude(id=id_article)[:5]
    return render(request,'detail.html',{"article":article,"aer":article_en_relation})
    
### Recherche sur un Article
def search(request):
    query=request.GET["article"]
    liste_article=Article.objects.filter(title__contains=query)
    return render(request,"search.html",{"liste_article":liste_article})

def sms(request):
    message=request.GET['body']
    message_splited=message.split("-")
    title=message_splited[0]
    desc=message_splited[1]
    
    agri_category=Category.objects.get(id=2)
    article= Article(title=title,category=agri_category,desc=desc,image="http://default")
    article.save()
    print('data saved successfully')
    return http.HttpResponse("data saved successfully")