from django.shortcuts import render,redirect
from .models import Contact
from django.contrib import messages

def contact(request):
	if request.method=="POST":
		listing_id = request.POST['listing_id']	
		name = request.POST['name']
		email = request.POST['email']
		phone = request.POST['phone']
		message = request.POST['message']
		user_id = request.POST['user_id']
		realtor_email = request.POST['realtor_email']
		listing = request.POST['listing']
		
		# checking if user has already made an inquiry
		if request.user.is_authenticated:
			user_id = request.user.id
			has_contacted = Contact.objects.all().filter(listing_id=listing_id, user_id=user_id)

			if has_contacted:
				messages.error(request,'You have already made this inquiry')
				return redirect(f'/listing/{listing_id}')

		contact = Contact(listing=listing, listing_id=listing_id, name=name, email=email, phone=phone, message=message,user_id=user_id)
		contact.save()

		messages.success(request,'Your request was successfull, Realtor will get back to you soon')

		return redirect(f'/listing/{listing_id}')
