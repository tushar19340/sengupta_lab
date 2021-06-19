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

    Papers_Category = models.Papers_Category.objects.all()    
    Papers = models.Paper.objects.all().order_by('-date')

    requested_filters = request.GET.getlist('filter_list')
    print("requested filters: ", requested_filters)
    
    if len(requested_filters) > 0:
        filtered_papers = []

        for p in Papers:
            categories = p.category.all()
            for categories in categories:
                # print(categories)
                # print(requested_filters)
                if categories.name in requested_filters:
                    filtered_papers.append(p)
                    break            
            Papers = filtered_papers

    context = {
        'papers': Papers,
        'filters': Papers_Category,
        'active_filters': requested_filters,
        'papers_page': 'active'
    }
    return render(request, 'papers.html', context)

def softwares(request):

    Software_Tags = models.Software_Tag.objects.all()
    softwares = models.Software.objects.all()

    requested_filters = request.GET.getlist('filter_list')
    print("requested filters: ", requested_filters)

    filtered_softwares = []
    if(len(requested_filters) > 0):
        for software in softwares:
            tags = software.tags.all()
            for tag in tags:
                # print(tag)
                # print(requested_filters)
                if tag.name in requested_filters:
                    filtered_softwares.append(software)
                    break            
            softwares = filtered_softwares

    context = {
        'softwares': softwares,
        'filters': Software_Tags,
        'active_filters': requested_filters,
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


