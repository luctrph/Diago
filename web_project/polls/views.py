from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    myname = "LUCTP"
    taisan1 =["dien thoai","xe may", "may tinh"]
    context = {"name":myname,"taisan":taisan1}
    
    return render(request,"polls/index.html",context)
