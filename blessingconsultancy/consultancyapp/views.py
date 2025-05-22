from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,"home.html")
<<<<<<< HEAD
def carrier(request):
    return render(request, "carrier.html")
=======
def client(request):
    return render(request, "client.html")
def service(request):
    return render(request, "service.html")

>>>>>>> cf9ac3d0e989d76fd4fe8c3841e66866acc7467b
