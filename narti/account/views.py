from .forms import LoginForm, UserRegistrationForm, FeedbackForm
from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from .models import Comics, Language
from .forms import FeedBack

menu = [{'title': 'Регистрация', 'url_name': 'register'},
        {'title': 'Войти', 'url_name': 'login'},
        {'title': 'О сайте', 'url_name': 'about'}
        ]


def index(request):
    comics = Comics.objects.all()
    # if len(comics) == 0:
    #     # raise Http404()
    index_context = {'comics': comics,
                     'menu': menu,
                     'title': 'Главная страница',
                     }
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
            return render(request, 'account/register-done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'account/register.html', {'user_form': user_form})


def about(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'account/about.html')
    else:
        form = FeedbackForm()
    return render(request, 'account/feedback_form.html', {'form': form})


def show_coms_id(request, coms_id):
    сomics_item = get_object_or_404(Comics, pk=coms_id)
    show_coms_id_context = {'menu': menu,
                            'title': 'Главная страница',
                            'comics_item': сomics_item,
                            }
    return render(request, 'account/comics.html', context=show_coms_id_context)


def show_lang_id(request, lang_id):
    return HttpResponse(f"Отображение комиксов с id = {lang_id}")


def language(request):
    lang_str = Language.objects.all()
    language_context = {'comics': comics,
                        'menu': menu,
                        'title': 'Главная страница',
                        'lang_str': lang_str,
                        }
    return render(request, 'account/language.html', context=language_context)


def lang_comics(request):
    if request.GET:
        queryprms = request.GET
        lang = queryprms.get('lang')
        search = queryprms.get('search')
        print(request.GET)
        filt_comics = Comics.objects.filter(language__abbr=lang, gender=search)
        lang_comics_context = {'comics': comics,
                               'menu': menu,
                               'title': 'Главная страница',
                               'filt_comics': filt_comics,
                               }
        return render(request, 'account/lang_comics.html', context=lang_comics_context)
    else:
        return render(request, 'account/lang_comics.html')


def comics(request):
    return render(request, 'account/comics.html')
