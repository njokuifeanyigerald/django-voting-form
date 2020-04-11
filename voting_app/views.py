from django.shortcuts import render, redirect
from .models import Vote
from .form import VotingForm


def home(request):
    form  =VotingForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            chosen_association_options = form.cleaned_data.get('chosen_association_options',[])
            other_association_name = form.cleaned_data.get('other_association_name', '')
            Vote.bulk_vote(chosen_association_options + [other_association_name])
            return redirect ('/')
    elif request.method == 'GET':
        message = ""
    context = {
        'form':form,
        'message':message,
    }
    return render(request, 'home.html', context)
