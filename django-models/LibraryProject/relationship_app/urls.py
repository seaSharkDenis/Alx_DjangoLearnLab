from django.contrib import admin
from django.urls import include, path
from django.contrib.auth.views import LogoutView
from django.contrib.auth.views import LoginView
from . import views
from .views import (list_books, LibraryDetailView, LibraryListView,
                    admin_view, librarian_view, member_view, add_book,
                    edit_book, delete_book)

urlpatterns = [
    path('books/', list_books, name='book-list'),
    path('libraries/', LibraryListView.as_view(), name='library-list'),
    path('library/<int:pk>', LibraryDetailView.as_view(), name='library-detail'),

    # Authentication URLs
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),

    # Role-based URLs
    path('admin/', admin_view, name='admin-view'),
    path('librarian/', librarian_view, name='librarian-view'),
    path('member/', member_view, name='member-view'),

    # Permission-secured URLs
    path('add_book/', add_book, name='add-book'),
    path('edit_book/<int:pk>/', edit_book, name='edit-book'),
    path('delete_book/<int:pk>/', delete_book, name='delete-book'),
]