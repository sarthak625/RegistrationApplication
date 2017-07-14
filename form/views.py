from django.shortcuts import render , HttpResponse , redirect
from form.forms import RegistrationForm
from rest_framework import generics
from serializers import UserSerializer
from django.contrib.auth.models import User

def home(request):
    return render(request,'form/home.html')

def register(request):
    if request.method == 'POST':
        print "POST"
        form = RegistrationForm(request.POST)

        if form.is_valid():
            print 'saved'
            form.save()
            return redirect('/account')
        else:
            return redirect('/account/register_fail')

    else:
        form = RegistrationForm()

        args = {'form' : form}
        return render(request,'form/reg_form.html',args)

def reg_fail(request):
    return render(request,'form/reg_fail.html')

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
