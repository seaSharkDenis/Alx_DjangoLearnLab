from django.contrib import admin
from django.urls import include, path
from . import views
from .views import book_list, LibraryDetailView, LibraryListView

urlpatterns = [
    path('books/', book_list, name='book-list'),
    path('libraries/', LibraryListView.as_view(), name='library-list'),
    path('library/<int:pk>', LibraryDetailView.as_view(), name='library-detail'),
]
