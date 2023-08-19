from django.shortcuts import redirect, render

from dojo_ninjas_app.models import Dojo, Ninja

# Create your views here.
def index(request):
    context = {
        "dojos": Dojo.objects.all(),
        "ninjas": Ninja.objects.all()
    }
    print("NINJAS**************",context["ninjas"].__dict__)
    print("DOJOS**************",context["dojos"].__dict__)
       
    return render(request, "index.html", context)

def create_dojo(request):
    new_dojo = {
        "name": request.POST['name'],
        "city": request.POST['city'],
        "state": request.POST['state']
    }
    Dojo.objects.create(name=new_dojo["name"], city=new_dojo["city"], state=new_dojo["state"])
    return redirect('/')

def create_ninja(request):
    Ninja.objects.create(
        first_name=request.POST['first_name'],
        last_name=request.POST["last_name"],
        dojo_id=request.POST["dojo_id"]
        )
    return redirect('/')

def delete_dojo(request):
    d = Dojo.objects.get(id=request.POST['id'])
    d.delete()
    return redirect('/')