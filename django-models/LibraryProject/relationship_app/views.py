from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import permission_required, user_passes_test
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Book, Author, UserProfile
from .models import Library

# Create your views here.

# Function-based view to list all books
def list_books(request):
    """View that displays all books"""
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-based view for library details
class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"

# Class-based view to list all libraries
class LibraryListView(ListView):
    model = Library
    template_name = "relationship_app/library_list.html"
    context_object_name = "libraries"

# --- Authentication Views ---
# Register view
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Set default role as Member for new users
            user_profile = UserProfile.obkjects.get(user=user)
            user_profile.role = 'Member'
            user_profile.save()

            login(request, user)  # log in new user
            messages.success(request, "Registration successful! You now have a member role.")
            return redirect("book-list")  # redirect to home page
    else:
        form = UserCreationForm()
    return render(request, "relationship_app/register.html", {"form": form})

# Login view
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Welcome back, {username}!")
                return redirect("book-list")
    else:
        form = AuthenticationForm()
    return render(request, "relationship_app/login.html", {"form": form})

# Logout view
def logout_view(request):
    logout(request)
    messages.info(request, "You have been logged out successfully.")
    return render(request, "relationship_app/logout.html")

# Check functions
def is_admin(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

def is_librarian(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

def is_member(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Member'

#Role Based Views
# Admin view
@login_required
@user_passes_test(is_admin)
def admin_view(request):
    users = User.objects.all()
    return render(request, "relationship_app/admin_view.html", {'users':users})

# Librarian view
@login_required
@user_passes_test(is_librarian)
def librarian_view(request):
    books = Book.objects.all()
    libraries = Library.objects.all()
    return render(request, "relationship_app/librarian_view.html",{
        'books':books,
        'libraries':libraries
    })

# Member view
@login_required
@user_passes_test(is_member)
def member_view(request):
    books = Book.object.all()
    return render(request, "relationship_app/member_view.html", {'books':books})

# Add book view
@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book-list')
    else:
        form = BookForm()
    return render(request, 'add_book.html', {'form': form})

# Edit book view
@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book-list')
    else:
        form = BookForm(instance=book)
    return render(request, 'edit_book.html', {'form': form})

# Delete book view
@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book-list')
    return render(request, 'delete_book.html', {'book': book})