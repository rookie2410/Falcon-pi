from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.views.generic import ListView
from django.views.generic import View
# Create your views here.
from .models import CrudUser
from django.http import JsonResponse


def index(request):
    return HttpResponse('<h1>heelo</h1>')

class CrudView(ListView):
    model = CrudUser
    template_name = 'crud_ajax/crud.html'
    context_object_name = 'users'


 

        
def input(request):
    return render(request,'crud_ajax/crud.html')


def savedata(request):
   
    
    if request.method =='POST':
        global funame1,fupass1,cncuser1,fuid1,cn1,monitport1
        funame1=request.POST['funame']
        fupass1=request.POST['fupass']
        cncuser1=request.POST['cncuser']
        fuid1=request.POST['username']
        cn1=request.POST['cncip']
        monitport1=request.POST['monitoringport']
        with open('file.txt', 'r') as file :
            filedata = file.read()
        return render(request,'crud_ajax/crud.html',{'fname':funame1,'cncuser':cncuser1,'fuid':fuid1})
        filedata = filedata.replace('funame',funame1)
        filedata = filedata.replace('pass', fupass1 )
        filedata = filedata.replace('fid', fuid1)
        filedata = filedata.replace('cnuser',cncuser1 )
        filedata = filedata.replace('cnip', cn1)
        filedata = filedata.replace('monitport', monitport1)
        
        with open('file.sh', 'w+') as file:
            file.write(filedata)
            filename = "{}.sh".format(funame1)
            response = HttpResponse(filedata, content_type='text/plain')
            response['Content-Disposition'] = 'attachment; filename={0}'.format(filename)
            return response
        
            # obj = CrudUser.objects.create(
            #     funame = funame1,
            #     fupass = fupass1,
            #     cn = cn1,
            #     cncuser=cncuser1,
            #     monitport= monitport1,
            #     fuid = fuid1,
            #     )
                
            #user = {'fname':obj.funame,'password':obj.password,'cn':obj.cn,'cncuser':obj.cncuser,'monitport':obj.monitport}
    


def down(request):
    with open('file.txt', 'r') as file :
            filedata = file.read()
    filedata = filedata.replace('funame',funame1)
    filedata = filedata.replace('pass', fupass1 )
    filedata = filedata.replace('fid', fuid1)
    filedata = filedata.replace('cnuser',cncuser1 )
    filedata = filedata.replace('cnip', cn1)
    filedata = filedata.replace('monitport', monitport1)
        
    with open('file.sh', 'w+') as file:
        file.write(filedata)
        filename = "{}.sh".format(funame1)
        response = HttpResponse(filedata, content_type='text/plain')
        response['Content-Disposition'] = 'attachment; filename={0}'.format(filename)
        return response
    
    

def shell(request):
    sshp=cncuser1+':'+fuid1
    return render (request,'crud_ajax/new.html',{'data':sshp})



