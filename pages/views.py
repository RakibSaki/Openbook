from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from .forms import PageForm
from .models import Page

# Create your views here.
@login_required
def home(request):
    return render(request, 'pages/home.html', {'pages':request.user.page_set.all()})

def login_view(request):
    message = ''
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(reverse_lazy('home'))
        else:
            message = 'Invalid Credentials'
    return render(request, 'registration/login.html', {'message':message})

class SignUp(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')

def logout_view(request):
    logout(request)
    return redirect(reverse_lazy('login'))

@login_required
def PageCreate(request):
    message = ''
    if request.method == 'POST':
        if PageForm({'content':request.POST['content']}).is_valid():
            page = Page(content=request.POST['content'], author=request.user)
            page.save()
            return redirect(reverse_lazy('home'))
        else:
            message = "Invalid page content"
    return render(request, 'pages/create.html', {
        'form':PageForm,
        'message':message
        })

@login_required
def PageUpdate(request, pk):
    message = ''
    page = None
    try:
        page = Page.objects.get(pk=pk)
    except Page.DoesNotExist:
        message = 'Page does not exist'
    if page.author != request.user:
        return render(request, 'pages/view.html', {'message': message})
    return render(request, 'pages/update.html', {'message': message, 'page': page})