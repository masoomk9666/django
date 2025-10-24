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
    return HttpResponse('Hello this is About Page')
def services(request):
    return HttpResponse('Hello this is Services Page')
def contact(request):
    return HttpResponse('Hello this is Contact Page')