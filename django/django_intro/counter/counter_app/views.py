from django.shortcuts import redirect, render

# Create your views here.
def counter(request):
    if 'count' in request.session:
        request.session['count'] += 1
    else: request.session['count'] = 1
    data = {
        "count": request.session['count']
    }
    return render(request,'index.html', data)

def reset_counter(request):
    del request.session['count']
    return redirect('/')

def add_by_2(request):
    request.session['count'] +=1
    return redirect('/')

def custom_add(request):
    print(request.POST)
    request.session['count'] += int(request.POST['increment']) - 1
    return redirect('/')
