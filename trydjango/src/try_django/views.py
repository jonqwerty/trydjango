from django.http import HttpResponse
from django.shortcuts import render



def home_page(request):
	my_title = "Hello there ............"
	context = {"title": "my title"}
	if request.user.is_authenticated:
		context = {"title": my_title, "my_list": [1,2,3,4,5]}
	return render(request, "home.html", context)


def about_page(request):
	return render(request, "about.html", {"title":"About Us"})


def contact_page(request):
	mes = 'Here is our contacts'
	message_not_auth = "If you see this. It means you must login for seen contacts"
	context = {"title": 'Contact Us', 'message':message_not_auth }
	if request.user.is_authenticated:
		context = {
			"title": 'Contact Us', 
			"message": mes, 
			"contacts": (('CEO', '32 64 36'), ('COO', '75 56 44' ), ('Sales', '76 90 30'))}

	return render(request, "contact.html", context)

