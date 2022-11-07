from django.shortcuts import render
from .forms import ContactForm
from products.views import Product
def home_page(request):
    print(request.session.get("first_name", "Unknown"))
    list = Product.objects.all()
    context = {
        'list': list
    }
    return render(request, "home_page.html")




def contact_page(request):
    contact_form = ContactForm(request.POST or None)

    context = {
        'form': contact_form
    }
    if contact_form.is_valid():
        print(contact_form.cleaned_data)
    return render(request, "contact/contact.html", context)