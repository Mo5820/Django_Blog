from django.contrib import messages
from django.shortcuts import redirect, render
from . forms import RegistrionForm
# Create your views here.
def register(request):
    if request.method=='POST':
        form=RegistrionForm(request.POST)
        if form.is_valid:
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,f'Account Created Done! {username}')
            return redirect('Blog Home')
        
    else:
        form=RegistrionForm()
    return render(request,'users/register.html',{'form':form})


