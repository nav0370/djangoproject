from django.shortcuts import render, HttpResponse
from contact import contact

# Create your views here. 
def index(request):
      context = {
          'variable1': "this is context text",
          'variable2': "this is context text",
          'variable3': "this is context text"
      }
      return render(request, 'index.html',context)
    # return HttpResponse("this is register page")

def about(request):
    return render(request, 'about.html')
    #return HttpResponse("this is about page")

def services(request):
    return render(request, 'services.html')
    #return HttpResponse("this is services page")

def contact(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        address = request.address.POST.get('address')
        contact = contact(email = email, password = password, address = address)
        contact.save()
    return render(request, 'contact.html')
    #return HttpResponse("this is contact page")
