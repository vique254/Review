from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, NewProjectForm, ProfileForm
from .models import Projects, Profile
from rest_framework import generics, status
from rest_framework.response import Response

# Create your views here.
@login_required(login_url='/login')
def index(request):
    current_user = request.user
    projects = Projects.get_projects()
    return render(request, 'index.html', {'current_user':current_user, 'projects':projects})

def signup(request):
    message = 'Login'
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'registration/registration_form.html', {'form': form, 'message':message})

@login_required(login_url='/login/')
def new_project(request):
    current_user = request.user
   
    if request.method == 'POST':
        form = NewProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.user= current_user
            project.save()
        return redirect('home')
    else:
        form = NewProjectForm()
    return render(request, 'new_project.html', {'current_user':current_user, 'form':form})

def profile(request):
    current_user = request.user

    projects = Projects.get_projects()
    
    return render(request, 'profile.html', {'current_user':current_user, 'projects':projects})

@login_required(login_url='/login/')
def update_profile(request):
    current_user = request.user
    profile = Profile(user=request.user)
   
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES,  instance=request.user.profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user= current_user
            profile.save()
        return redirect('home')
    else:
        form = ProfileForm(instance=request.user.profile)
        args = {}
        # args.update(csrf(request))
        args['form'] = form
    return render(request, 'update_profile.html', {'current_user':current_user, 'form':form})


    def post(self,request):
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def search_results(request):

        if 'article' in request.GET and request.GET["article"]:
            search_term = request.GET.get("article")
            searched_articles = Article.search_by_title(search_term)
            message = f"{search_term}"

            return render(request, 'all-news/search.html',{"message":message,"articles": searched_articles})

        else:
            message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})
