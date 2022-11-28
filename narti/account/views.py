from .forms import LoginForm, UserRegistrationForm
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from .models import Comics

menu = [{'title': 'Регистрация', 'url_name': 'register'},
        {'title': 'Войти', 'url_name': 'login'},
        {'title': 'О сайте', 'url_name': 'about'}
        ]


def index(request):
    comics = Comics.objects.all()
    index_context = {'comics': comics,
                     'menu': menu,
                     'title': 'Главная страница'}
    return render(request, 'account/index.html', context=index_context)


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            return render(request, 'account/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'account/register.html', {'user_form': user_form})


def about(request):
    about_context = {'menu': menu,
                     'title': 'О сайте'}
    return render(request, 'account/about.html', context=about_context)


def show_coms_id(request, coms_id):
    return HttpResponse(f"Отображение комиксов с id = {coms_id}")


def language(request):
    return HttpResponse(f"Отображение языков")


def lang_comics(request):
    return HttpResponse(f"Отображение комиксов по языкам")

