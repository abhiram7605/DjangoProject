import json
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from . models import UserDetails
from . serializers import UDserializer
from. forms import UDform, UDsigninform
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
@csrf_exempt
def signin(request):
    if request.method == "POST":
        form = UDsigninform(request.POST)
        print(form)
        if form.is_valid():
            email= form.cleaned_data["Email"]
            password = form.cleaned_data["Password"]
            try:
                user = UserDetails.objects.get(Email= email)
                if user.Password == password:
                    return HttpResponse("User Successfully loggedIn")
                else:
                    return HttpResponse("Wrong Password")
            except:
                return HttpResponse("User Doesnot Exist")
        else:
            return HttpResponse("Wrong submission")
        
    else:
        form= UDsigninform()
    
    return render(request, "Loginify/userdata.html", {"form": form})
        




    
