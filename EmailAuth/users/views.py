from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from .forms import LoginEmail, GoalsForm
from .models import Goal
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q

def login(request):
    if not request.user.is_authenticated():
        if request.method == 'POST':
            loginform = LoginEmail(request.POST)
            if loginform.is_valid():
                email = loginform.cleaned_data['email']
                try:
                    username = User.objects.get(email=email.lower()).username
                except:
                    return render(request, 'login.html', {'error':'Not a Valid Email Address', 'form':loginform})
                user = auth.authenticate(username = username, password = loginform.cleaned_data['password'])
                if user is not None:
                    auth.login(request, user)
                    return redirect('home')
                else:
                    return render(request, 'login.html', {'error':'Email or Password incorrect', 'form':loginform})
        else:
            loginform = LoginEmail()
            return render(request, 'login.html', {'form':loginform})
    else:
        return redirect('NOTlogin')

def invalid(request):
    return render(request, 'NOTlogin.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('login')

@login_required()
def create(request):
    if request.method == 'POST':
        form = GoalsForm(request.POST)
        if form.is_valid():
            Goal.objects.create(
                user=request.user,
                title=form.cleaned_data["title"],
                description=form.cleaned_data["description"],
            )
            return redirect('home')
    else:
        form = GoalsForm()
    return render(request, 'create.html', {'form':form})

def home(request):
    if request.user.is_authenticated():
        goals = Goal.objects.filter(user=request.user)

        paginator = Paginator(goals, 3)
        page = request.GET.get('page')

        try:
            items = paginator.page(page)
        except PageNotAnInteger:
            items = paginator.page(1)
        except EmptyPage:
            items = paginator.page(paginator.num_pages)

        index = items.number - 1
        max_index = len(paginator.page_range)
        start_index = index - 5 if index >= 5 else 0
        end_index = index + 5 if index <= max_index - 5 else max_index
        page_range = paginator.page_range[start_index:end_index]


        return render(request, 'home.html', {'items':items, 'page_range':page_range})
    else:
        return render(request, 'home.html')


@login_required()
def update(request, pk):
    goal = Goal.objects.get(id=pk , user=request.user)
    if request.method == 'POST':
        print('inside post')
        form = GoalsForm(request.POST)
        if form.is_valid():
            print('inside')
            goal.title = form.cleaned_data["title"]
            goal.description = form.cleaned_data["description"]
            goal.save()
            return redirect('home')
    else:
        form = GoalsForm(initial={'title': goal.title, 'description': goal.description})
    return render(request, 'edit.html', {'form':form})


@login_required()
def destroy(request, pk):
    goal = Goal.objects.get(id=pk)
    goal.delete()
    return redirect('home')

@login_required()
def search(request):
    query = request.GET.get('q')

    goals = Goal.objects.filter(Q(title__icontains = query)| Q(description__icontains = query))

    paginator = Paginator(goals, 3)
    page = request.GET.get('page')

    try:
        items = paginator.page(page)
    except PageNotAnInteger:
        items = paginator.page(1)
    except EmptyPage:
        items = paginator.page(paginator.num_pages)

    index = items.number - 1
    max_index = len(paginator.page_range)
    start_index = index - 5 if index >= 5 else 0
    end_index = index + 5 if index <= max_index - 5 else max_index
    page_range = paginator.page_range[start_index:end_index]

    return render(request, 'home.html', {'items':items, 'page_range':page_range})



