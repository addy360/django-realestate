from django.shortcuts import render, get_object_or_404
from .models import Listing
from django.core.paginator import PageNotAnInteger, Paginator,EmptyPage


def index(request):
	listings = Listing.objects.order_by('-list_date').filter(is_published=True)
	paginator = Paginator(listings , 6)
	page = request.GET.get('page')
	paged_listing = paginator.get_page(page)
	context = {
		'listings' : paged_listing
	}
	return render(request , 'listings/listings.html', context)

def listing(request,listing_id):
	listing = get_object_or_404(Listing,pk=listing_id)
	context = {
		'listing' : listing
	}
	return render(request, 'listings/listing.html' , context)	

def search(request):
	search_results = Listing.objects.all().order_by('-list_date')

	if 'keywords' in request.GET:
		keywords = request.GET['keywords']
		if keywords:
			search_results = search_results.filter(description__icontains=keywords)

	if 'city' in request.GET:
		keywords = request.GET['city']
		if keywords:
			search_results = search_results.filter(city__iexact=keywords)		

	if 'state' in request.GET:
		keywords = request.GET['state']
		if keywords:
			search_results = search_results.filter(state__iexact=keywords)	
			
	if 'bedrooms' in request.GET:
		keywords = request.GET['bedrooms']
		if keywords:
			search_results = search_results.filter(bedrooms__lte=keywords)

	if 'price' in request.GET:
		keywords = request.GET['price']
		if keywords:
			search_results = search_results.filter(price__lte=keywords)					
	context = {
		'results': search_results
	}
	return render(request , 'listings/search.html', context)