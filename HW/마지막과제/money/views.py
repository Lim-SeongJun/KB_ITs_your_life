from django.shortcuts import render, reverse

from money.models import Money

# Create your views here.
def index(request):
    count = len(Money.objects.all())
    ctx={"count":count}
    return render(request, "../templates/index.html",ctx)

from django.views.generic.edit import CreateView
class InMoneyCreateView(CreateView):
    model = Money
    fields = ["title","money"]
    template_name = "../templates/increate.html" # 앱이름/모델명_form.html

    def get_success_url(self):
        return reverse("main")  # viewname

class OutMoneyCreateView(CreateView):
    model = Money
    fields = ["title","money"]
    template_name = "../templates/outcreate.html" # 앱이름/모델명_form.html

    def get_success_url(self):
        return reverse("main")  # viewname

from django.views.generic.list import ListView
class MoneyListView(ListView):
    model = Money
    ordering = "-pk"
    template_name = "../templates/list.html" 

from django.views.generic.detail import DetailView
class MoneyDetailView(DetailView):
    model = Money
    template_name = "../templates/detail.html" 
from django.views.generic.edit import DeleteView
