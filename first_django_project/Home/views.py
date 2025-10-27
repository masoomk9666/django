from django.shortcuts import render, HttpResponse
from Home.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    context = {
        "Name":"Saad Ali",
        "experties": "Senior Website Developer • WordPress , Python django , php & Front end"
    }
    return render(request, "index.html", context)
    # return HttpResponse('Hello this is Home Page')
def about(request):
    return render(request, "about.html")
def services(request):
        return render(request, "services.html")

def skills(request):
        return render(request, "skills.html")
def experience(request):
        return render(request, "experience.html")
def contact(request):
        if request.method == "POST":
               name = request.POST.get('name')
               email = request.POST.get('email')
               phone = request.POST.get('phone')
               message = request.POST.get('message')
               contact = Contact(name=name, email=email, phone=phone, message=message)
               contact.save()
               messages.success(request, "Your Form Submission Succesful.")
               
        return render(request, "contact.html")
