from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.views.generic import ListView
from django.views.generic import View
# Create your views here.
from .models import CrudUser
from django.http import JsonResponse

def index(request):
    return HttpResponse('<h1>heelo</h1>')


class CreateCrudUser(View):
    def  get(self, request):
        dfuname = request.GET.get('funame', None)
        dfupass = request.GET.get('fupass', None)
        dcncip = request.GET.get('cncip', None)
        dcncuser = request.GET.get('cncuser', None)
        dmonitoringport = request.GET.get('monitoringport', None)
        dUsername = request.GET.get('Username', None)
 

        
def input(request):
    return render(request,'crud_ajax/crud.html')


def savedata(request):
    if request.method =='POST':
        funame=request.POST['funame']
        fupass=request.POST['fupass']
        cncuser=request.POST['cncuser']
        username=request.POST['username']
        cn=request.POST['cncip']
        monitport=request.POST['monitoringport']
        with open('file.txt', 'r') as file :
            filedata = file.read()

        filedata = filedata.replace('funame',funame)
        filedata = filedata.replace('pass', fupass )
        filedata = filedata.replace('fid', cncuser)
        filedata = filedata.replace('cnuser',username )
        filedata = filedata.replace('cnip', cn)
        filedata = filedata.replace('monitport', monitport)

        with open('file.sh', 'w+') as file:
            file.write(filedata)
            filename = "{}.sh".format(funame)
            response = HttpResponse(filedata, content_type='text/plain')
            response['Content-Disposition'] = 'attachment; filename={0}'.format(filename)
            return response
            
            








##  "funame"
##  "pass"
## "fid"
## "cnuser"
##"cnip"
##"monitport"

    
