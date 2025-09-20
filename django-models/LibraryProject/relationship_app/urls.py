from django.contrib import admin
from django.urls import include, path
from .views import list_books, LibraryDetailView, LibraryListView, register_view, login_view, logout_view

urlpatterns = [
    path('books/', list_books, name='book-list'),
    path('libraries/', LibraryListView.as_view(), name='library-list'),
    path('library/<int:pk>', LibraryDetailView.as_view(), name='library-detail'),

    # Authentication URLs
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]
