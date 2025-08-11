from django.shortcuts import render, redirect, get_object_or_404
from .models import Listing
from .forms import ListingForm

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

    favorited_listings = request.session.get('favorites', [])

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

    context = {
        'form': form
    }
    return render(request, 'create_listing.html', context)

def product_detail(request, product_id):
    product = get_object_or_404(Listing, id=product_id)
    favorites_list_ids = request.session.get('favorites', [])
    
    context = {
        'product': product,
        'is_favorited': product.id in favorites_list_ids,
    }
    return render(request, 'product_detail.html', context)

def toggle_favorite(request, listing_id):
    favorites_list = request.session.get('favorites', [])
    
    if listing_id in favorites_list:
        favorites_list.remove(listing_id)
    else:
        favorites_list.append(listing_id)

    request.session['favorites'] = favorites_list
    
    return redirect(request.META.get('HTTP_REFERER', 'product_list'))

def favorite_list(request):
    favorites_list_ids = request.session.get('favorites', [])
    favorites = Listing.objects.filter(id__in=favorites_list_ids)
    
    context = {
        'favorites': favorites
    }
    return render(request, 'favorite_list.html', context)