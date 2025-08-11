from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.conf import settings
from .models import Listing, Favorite
from .forms import ListingForm
from django.contrib.auth.models import User 


def product_list(request):
    search_query = request.GET.get('search_query')
    location_query = request.GET.get('location')
    category_query = request.GET.get('category')

    listings = Listing.objects.all()

    if search_query:
        listings = listings.filter(title__icontains=search_query)

    if location_query:
        listings = listings.filter(location__icontains=location_query)

    if category_query:
        listings = listings.filter(category=category_query)

    # Get a list of favorited listing IDs for the current user
    if request.user.is_authenticated:
        favorited_listings = Favorite.objects.filter(user=request.user).values_list('listing_id', flat=True)
    else:
        favorited_listings = []

    context = {
        'products': listings,
        'search_query': search_query or '',
        'location_query': location_query or '',
        'category_query': category_query or '',
        'categories': Listing.CATEGORY_CHOICES,
        'favorited_listings': favorited_listings,
    }
    return render(request, 'product_list.html', context)

def create_listing(request):
    if request.method == 'POST':
        form = ListingForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ListingForm()
    
    return render(request, 'create_listing.html', {'form': form})


def favorite_listing(request, listing_id):
    listing = get_object_or_404(Listing, id=listing_id)
    favorite, created = Favorite.objects.get_or_create(user=request.user, listing=listing)
    
    if not created:
        # If the favorite already existed, delete it (un-favorite)
        favorite.delete()
    
    return redirect('product_list')


def favorite_list(request):
    favorites = Favorite.objects.filter(user=request.user).select_related('listing')
    return render(request, 'favorite_list.html', {'favorites': favorites})

def product_detail(request, product_id):
    product = get_object_or_404(Listing, id=product_id)
    context = {
        'product': product
    }
    return render(request, 'product_detail.html', context)

def create_listing(request):
    if request.method == 'POST':
        form = ListingForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ListingForm()

    context = {
        'form': form
    }
    return render(request, 'create_listing.html', context)
