from django.shortcuts import render,HttpResponse
def home(request):
    return render(request, 'home.html')

#def index(request):
  #  context={
   #     'variable': "Techo orienter"
    #}
    #return render(request,'index.html', context)
    #return HttpResponse("this is the Home Page")

def about(request):
    return render(request,'about.html' )

def services(request):
    return render(request,'services.html' )

    
def contact(request):
    
    return render(request,'contact.html' )