from django.urls import path
from sort.views import Home
from . import views

urlpatterns = [
    path('home/', Home.as_view(),name="home"),
    path('results/',views.list_sort,name="results"),
]
