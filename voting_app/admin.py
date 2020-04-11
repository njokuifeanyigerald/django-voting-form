from django.contrib import admin
from .models import Vote



class VoteAdmin(admin.ModelAdmin):
    model = Vote
    list_display = ['association_name','vote_count']
    list_filter = ['association_name']
    search_fields = ['association_name']

    def vote_count(self, obj):
        if obj.vote < 2:
            return "{} vote".format(obj.vote)
        return "{} votes".format(obj.vote)
admin.site.register(Vote, VoteAdmin)