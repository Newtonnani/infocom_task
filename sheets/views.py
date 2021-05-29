from django.http.response import HttpResponse
import sheets
from django.shortcuts import redirect, render
from .models import Sheet
from .models import SheetData
# Create your views here.

def index(request):
    return render(request,'create.html')


def data(request):
    if request.method == 'POST':
        rows = request.POST.get('rows')
        columns = request.POST.get('columns')
        Sheet.objects.all().delete()
        sheet = Sheet(rows=rows,columns=columns)
        sheet.save()
        return redirect('/')
    else:
        return render(request,'data.html')

def data_submit(request):
    if request.method == 'POST':
        SheetData.objects.all().delete()
        print(request.POST['data[]'])
        data = request.POST.get('data[]')
        final_data = ' '.join(data)
        
        sheet_data = SheetData(data=final_data)
        sheet_data.save()
        return redirect('/')
    return HttpResponse("<h1>Not a preferred method</h1>")