from django.shortcuts import render

# Create your views here.
from django.core.paginator import Paginator
from .models import initiative
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .forms import *
from django.contrib.auth.decorators import login_required

def home(request):
    initiative_list = initiative.objects.all().order_by('-id')

    paginator = Paginator(initiative_list, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(
        request,'main/home.html',{'page_obj': page_obj})
def about(request):
    return render(request, "main/about.html")
def profile(request):
    return render(request, "main/user.html")

@login_required
def initiativ(request):
    if request.method == 'POST':
        form = InitiativeForm(request.POST, request.FILES)
        if form.is_valid():
            ini = form.save(commit=False)
            ini.offering = request.user
            ini.save()
            return redirect('home')
    else:
        form = InitiativeForm()

    return render(request, 'main/initiative.html', {'form': form})


def inc(request, pk):
    ini = get_object_or_404(initiative, pk = pk)
    comments = ini.comments.all()
    return render(request, "main/inc.html", {"initiative" : ini, "comments": comments})

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'main/register.html', {'form': form})
@login_required
def add_comment(request, initiative_id):
    ini = get_object_or_404(initiative, id=initiative_id)

    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.relin = ini
            comment.save()

            return redirect('initiativeCard', initiative_id)
    else:
        form = CommentForm()

    return render(request, 'main/comments.html', {
        'form': form,
        'initiative': initiative
    })