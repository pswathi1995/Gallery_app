from django.shortcuts import render
from .models import Sign
#from .forms import SignUpForm

# Create your views here.
def home(request):
    print 'hello'
    if request.method == 'POST':
        #form = SignUpForm(request.POST)
        email = request.POST.get('email')
        name = request.POST.get('name')
        print email,name
        SignUp_obj = Sign(email=email, name=name)
        SignUp_obj.save()
    else:
        print 'hello----'
        #form = SignUpForm()
    title = "My Title"
    context = {
        "template":title,
        #"form":form
    }
    #return data(request)
    return render(request, 'home.html', context)

def data(request):
    data = Sign.objects.all()
    return render(request, 'data.html', {"cont":data})
