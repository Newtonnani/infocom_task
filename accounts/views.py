from typing import Counter
import sheets
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from sheets.models import Sheet
# Create your views here.


def login(request):
    if request.method == "POST":
        if (request.POST.get('username')) == "INFOCOM" and (request.POST.get('password')) == "1234":
            return 
        else:
            return redirect('login')
    else:
        return render(request,'loginform.html')

def loggedin(request):
    sheet_obj = Sheet.objects.first()
    if sheet_obj:
        rows = sheet_obj.rows
        columns = sheet_obj.columns
        context = {
            'rows':range(1,rows+1),
            'columns':range(1,columns+1)
        }
        return render(request,'sheet.html',context)
    
    return HttpResponse("<h1>LOGGED IN DATA NOT PRESENT</h1>")