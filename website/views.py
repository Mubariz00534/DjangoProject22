from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, get_user_model
from . import forms

def home_page(request):
    context = {
        'title': 'title'
    }
    if request.user.is_authenticated: 
        context['vip_content'] = 'Vip Content'
    return render(request, 'home_page.html', context)

def contact_page(request):
    contact_form = forms.ContactForm(request.POST or None)
    
    if contact_form.is_valid():
        print(contact_form.cleaned_data)

    # if request.method == 'POST':
    #     print("This is post:",request.POST)   
    return render(request, 'contact/view.html', {'title': 'Contact Page', 'form': contact_form})

def login_page(request):
    form = forms.LoginForm(request.POST or None)
    context = {
        'form': form
    }

    if form.is_valid():
        # print(form.cleaned_data) {'username': 'Mubariz', 'password': '43242342'}
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('/')
        else: 
            print("errrorrrrrrrrrrrrrrrrrrrrrrrrrrrr")
    return render(request, 'auth/login.html', context)

User = get_user_model()
def register_page(request):
    form = forms.RegisterForm(request.POST or None)

    context = {
        'form': form
    }

    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get("username")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")

        new_user = User.objects.create_user(username, email, password)
        print(new_user)

    return render(request, 'auth/register.html', context)