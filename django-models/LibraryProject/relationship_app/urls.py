from django.contrib import admin
from django.urls import include, path
from django.contrib.auth.views import LogoutView
from django.contrib.auth.views import LoginView
from .views import list_books, LibraryDetailView, LibraryListView, register

urlpatterns = [
    path('books/', list_books, name='book-list'),
    path('libraries/', LibraryListView.as_view(), name='library-list'),
    path('library/<int:pk>', LibraryDetailView.as_view(), name='library-detail'),

    # Authentication URLs
    path('register/', register, name='register'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
]
