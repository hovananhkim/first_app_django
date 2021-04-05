from django.urls import path
from .views import homePageView, detailPage
urlpatterns = [
    path ("",homePageView, name = 'home'),
]