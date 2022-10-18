from django.shortcuts import render,reverse
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from article.models import Article
# Create your views here.

def index(request):
    count = len(Article.objects.all())
    ctx = {"count":count}
    return render(request,"article/index.html",ctx)

class ArticleCreateView(CreateView):
    model = Article
    fields = ["title","content"]
    template_name = "article/create.html" # 앱이름/모델명
    success_url = "/article/" #포워드
    def get_success_url(self):
        return reverse("main")  # viewname

class ArticleListView(ListView):
    model = Article
    template_name = "article/list.html"