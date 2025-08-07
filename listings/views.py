# thrifty/listings/views.py

from django.shortcuts import render, redirect

from .models import Product
from .forms import ProductForm
from django.db.models import Q

def product_list(request):
    search_query = request.GET.get('search_query')
    location_query = request.GET.get('location')

    products = Product.objects.all()

    if search_query:
        products = products.filter(
            Q(title__icontains=search_query) |
            Q(description__icontains=search_query) |
            Q(category__icontains=search_query)
        )

    if location_query:
        products = products.filter(location__icontains=location_query)

    context = {
        'products': products
    }
    return render(request, 'listings/product_list.html', context)

# The create_listing view remains the same
def create_listing(request):
    # ... (your existing create_listing code)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            listing = form.save(commit=False)
           
            listing.save()
            return redirect('product_list')
    else:
        form = ProductForm()

    context = {
        'form': form
    }
    return render(request, 'listings/create_listing.html', context)

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login') # Redirects to the login page after successful signup
    else:
        form = UserCreationForm()

    context = {'form': form}
    return render(request, 'registration/signup.html', context)