"""
@author: jcachaldora
urls.py - Defines urls with /table/ base 
"""
from django.contrib import admin
from django.urls import path
from . import views

app_name = 'table'
urlpatterns = [
    path('', views.IndexView, name='table'),
    path('filterform/', views.FilterView, name='filterform'),
    path('admin/', admin.site.urls),
    path('results/', views.ResultsView, name='results'),
    path('search/', views.SearchView, name='search'),
    path('searchresults/', views.SearchResultsView, name='searchresults'),
    path('searchbycoord/', views.SearchCoordView, name = 'searchcoord'),
    path('testplot/', views.TestView, name='testplot'),
    #generic path for spectra profiles
    path('<str:source_id>/', views.DetailView, name='detail'),
]

