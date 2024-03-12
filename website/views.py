from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
from .models import Record
# Create your views here.

def home(request):
    records = Record.objects.all()



    # check si quelqu'un est loggé
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        #autentification
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Vou avez été Loggé")
            return redirect('home')
        else:
            messages.success(request, "Il y a eu un error dans le login, reessayez postieurement")
            return redirect('home')
    else:
        return render(request, 'home.html', {'records':records})

def logout_user(request):
    logout(request)
    messages.success(request, "Vous avez logout")
    return redirect('home')


def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            #autentification et login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "Vous avez bien ete enregistré")
            return redirect('home')
        
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form':form})
    
    return render(request, 'register.html', {'form':form})


def costumer_record(request, pk):
    if request.user.is_authenticated:
        # chercher les registres
        costumer_record = Record.objects.get(id=pk)
        return render(request, 'record.html', {'costumer_record':costumer_record})
    
    else:
        messages.success(request, "Vous devez vous logger pour avoir cette information")
        return redirect('home')
    

def delete_record(request, pk):
    if request.user.is_authenticated:
        delete_it = Record.objects.get(id=pk)
        delete_it.delete()
        messages.success(request, "Vous devez effacé ce document")
        return redirect('home')
    else:
        messages.success(request, "Vous devez vous logger pour faire ça")
        return redirect('home')
    


def add_record(request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_record = form.save()
                messages.success(request, "Registre enregistré")
                return redirect('home')
        return render(request, 'add_record.html', {'form': form})
    else:
        messages.success(request, "Vous devez vous connecter pour faire ça")
        return redirect('home')
    



def update_record(request, pk):
    if request.user.is_authenticated:
        current_record = Record.objects.get(id=pk)
        form = AddRecordForm(request.POST or None, instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request, "Registre enregistré")
            return redirect('home')
        return render(request, 'update_record.html', {'form': form})
    else:
        messages.success(request, "Vous devez vous connecter pour faire ça")