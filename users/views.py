from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password, make_password
from .models import User

def login_view(request):
    if request.method == 'POST':
        name = request.POST['name']
        password = request.POST['password']
        try:
            user = User.objects.get(name=name)
            if check_password(password, user.password):
                request.session['user_id'] = user.id
                return redirect('skins_list')  # Redireciona para a página inicial ou dashboard
            else:
                return render(request, 'login.html', {'error_message': 'Senha inválida'})
        except User.DoesNotExist:
            return render(request, 'login.html', {'error_message': 'Usuário não encontrado'})
    return render(request, 'login.html')

def signup_view(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        password = make_password(request.POST['password'])
        if User.objects.filter(name=name).exists():
            return render(request, 'signup.html', {'error_message': 'Usuário já existe'})
        user = User(name=name, email=email, phone_number=phone_number, password=password)
        user.save()
        return render(request, 'login.html', {'success_message': 'Cadastro realizado com sucesso!'})
    return render(request, 'signup.html')