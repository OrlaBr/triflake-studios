from django.shortcuts import render
from django.views.generic import View
from django.views.generic import TemplateView


# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'


class PortfolioPageView(TemplateView):
    template_name = 'portfolio.html'


class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "pages/home.html", {})
