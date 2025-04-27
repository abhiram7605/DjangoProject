import json
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from . models import UserDetails
from . serializers import UDserializer
from. forms import UDform
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect

def hello(request):
    return HttpResponse("Hello world")


@csrf_exempt

def signup(request):

    if request.method =="POST":
        try:
            form = UDform(request.POST)
            if form.is_valid():
                form.save()
                return redirect('signin')
        except Exception as e:
            return JsonResponse({
                "Success": False,
                "Message": str(e)
            })
    else:
        form = UDform()
    
    return render(request, "Loginify/userdata.html", {"form": form})

def signin(request):
    return HttpResponse("Hi, Successfully signedIN")
    
