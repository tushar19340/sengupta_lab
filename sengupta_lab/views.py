from django.shortcuts import render, HttpResponse
from sengupta_lab import models

def index(request):
    home = models.Home.objects.all()
    if(len(home) > 0):
        home = home[len(home) - 1]
    
    context = {
        'home': home
    }
    
    return render(request, 'index.html', context)

def research(request):
    research = models.Research.objects.all()

    context = {
        'research': research
    }
    
    return render(request, 'research.html', context)
    
def team(request):
    team = models.Team.objects.all()
    context = {
        'team': team
    }

    return render(request, 'team.html', context)

def papers(request):

    papers = models.Paper.objects.all().order_by('-date')
    context = {
        'papers': papers
    }
    return render(request, 'papers.html', context)

def softwares(request):
    softwares = models.Software.objects.all()
    context = {
        'softwares': softwares
    }
    return render(request, 'softwares.html', context)

def news(request):
    news = models.News.objects.all()
    context = {
        'news': news
    }
    return render(request, 'news.html', context)

def about(request):
    about = models.About.objects.all()
    if(len(about) > 0):
        about = about[len(about) - 1]
    context = {
        'about': about
    }
    return render(request, 'about.html', context)


