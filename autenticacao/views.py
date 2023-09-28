from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect


# Create your views here.
def logar(request):
    if request.method=="POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            senha = form.cleaned_data.get('password')

            user = authenticate(username=usuario, password=senha)
            if user is not None:
                login(request, user)
                messages.info(request, f"Seja bem vindo, {user.username}")
                return redirect("index")
            else:
                messages.info(request, "Usuário ou senha inválido.")
        else:
            messages.info(request, "Usuário ou senha inválido.")
    form = AuthenticationForm()
    return render(request, 'login.html', {'login_form': form})


def registro(request):
    return render(request, 'registro.html')


def sair(request):
    logout(request)
    return redirect('index')