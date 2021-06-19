from django.contrib import admin
from sengupta_lab.models import Home, Paper, Research, Team, Software, News, About, Footer, Software_Tag

# Register your models here.
admin.site.register(Home)
admin.site.register(Paper)
admin.site.register(Research)
admin.site.register(News)
admin.site.register(Team)
admin.site.register(About)
admin.site.register(Footer)

class Software_TagAdmin(admin.ModelAdmin):
    filter_horizontal = ('tags',)

admin.site.register(Software_Tag)
admin.site.register(Software, Software_TagAdmin)

