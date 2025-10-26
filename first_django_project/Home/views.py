from django.shortcuts import render, HttpResponse

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
        return render(request, "contact.html")
