from django.contrib import admin
from sengupta_lab.models import Home, Paper, Papers_Category, Research, Team, Member_Type,  Software, News, About, Footer, Software_Tag

# Register your models here.
admin.site.register(Home)
admin.site.register(Research)
admin.site.register(News)
admin.site.register(About)
admin.site.register(Footer)

class Software_TagAdmin(admin.ModelAdmin):
    filter_horizontal = ('tags',)


admin.site.register(Software_Tag)
admin.site.register(Software, Software_TagAdmin)

class PapersAdmin(admin.ModelAdmin):
    filter_horizontal = ('category',)

admin.site.register(Paper, PapersAdmin)
admin.site.register(Papers_Category)

class TeamAdmin(admin.ModelAdmin):
    filter_horizontal = ('member_type',)

admin.site.register(Team, TeamAdmin)
admin.site.register(Member_Type)