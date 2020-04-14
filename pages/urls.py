from django.contrib import admin
from django.urls import path, include
from .views import HomePageView, PortfolioPageView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),
    path('', HomePageView.as_view(), name='home'),
    path('portfolio/', PortfolioPageView.as_view(), name='portfolio'),
]
