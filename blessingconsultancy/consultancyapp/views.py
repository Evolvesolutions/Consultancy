from django.shortcuts import render,redirect

from .forms import contact,careerApplicationform

# Create your views here.
def home(request):
    return render(request,"home.html")
# def client(request):
#     return render(request, "client.html")
# def service(request):
#     return render(request, "service.html")
def carrier(request):
    return render (request,'carrier.html')

def submit (request):
       if request.method =='POST':
            form = contact(request.POST)
            if form.is_valid():
                 form.save()
                 return redirect('registration_success')
            else:
                 form = contact()
            return render (request,'home.html',{'form':form})


def registration_success(request):
        return render (request,"success.html")


def submission(request):
     if request.method == 'POST':
          form = careerApplicationform(request.POST, request.FILES)
          if form.is_valid():
               form.save()
               return redirect('registration_success')

          else:
               form = careerApplicationform()
          return render (request,'carrier.html',{'form':form})

     




