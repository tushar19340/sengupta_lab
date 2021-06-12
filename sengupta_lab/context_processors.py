from django.shortcuts import render, HttpResponse
from sengupta_lab import models

def fetch_footer(request):
    footer = models.Footer.objects.all()
    if(len(footer) - 1 >= 0):
        footer = footer[len(footer) - 1]

    return {
        'footer': footer
    }