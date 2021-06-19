from django.shortcuts import render, HttpResponse
from sengupta_lab import models

def index(request):
    home = models.Home.objects.all()
    if(len(home) > 0):
        home = home[len(home) - 1]
    
    context = {
        'home': home,
        'home_page': 'active'
    }
    
    return render(request, 'index.html', context)

def research(request):
    research = models.Research.objects.all()

    context = {
        'research': research,
        'research_page': 'active'
    }
    
    return render(request, 'research.html', context)
    
def team(request):
    team = models.Team.objects.all()
    context = {
        'team': team,
        'team_page': 'active'
    }

    return render(request, 'team.html', context)

def papers(request):

    papers = models.Paper.objects.all().order_by('-date')
    context = {
        'papers': papers,
        'papers_page': 'active'
    }
    return render(request, 'papers.html', context)

def softwares(request):

    Software_Tags = models.Software_Tag.objects.all()
    
    softwares = models.Software.objects.all()


    if request.method == "POST":
        requested_filters = request.POST.getlist('filter_list')
        filtered_softwares = []

        for software in softwares:
            software_tags = software.tags.all()
            for tag in software_tags:
                # print(tag)
                # print(requested_filters)
                if tag.name in requested_filters:
                    filtered_softwares.append(software)
                    break            
            softwares = filtered_softwares

    context = {
        'softwares': softwares,
        'filters': Software_Tags,
        'software_page': 'active'
    }
    return render(request, 'softwares.html', context)

def news(request):
    news = models.News.objects.all()
    context = {
        'news': news,
        'news_page': 'active'
    }
    return render(request, 'news.html', context)

def about(request):
    about = models.About.objects.all()
    if(len(about) > 0):
        about = about[len(about) - 1]
    context = {
        'about': about,
        'about_page': 'active'
    }
    return render(request, 'about.html', context)


