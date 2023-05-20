from django.shortcuts import render
from basicapp.forms import NewUser

# Create your views here.

def index(request):
    return render(request, "basicapp/index.html")

def user(request):

    form=NewUser()

    if request.method== "POST":
        form=NewUser(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)

        else:
            print("Error")
    
    return render(request, 'basicapp/form.html',{'form':form})