from django.contrib import admin
from django.urls import include, path
from .views import list_books, LibraryDetailView, LibraryListView

urlpatterns = [
    path('books/', list_books, name='book-list'),
    path('libraries/', LibraryListView.as_view(), name='library-list'),
    path('library/<int:pk>', LibraryDetailView.as_view(), name='library-detail'),
]
