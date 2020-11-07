from django.shortcuts import render
from django.http import HttpResponseRedirect
from django import forms
from django.urls import reverse
from . import customforms
from .import database
from . import config
import re
# from django import forms


def index(request):
    if request.method=='POST':       
        form=customforms.Team(request.POST)
        if form.is_valid():
            config.teams.append(form.cleaned_data['team1'])
            config.teams.append(form.cleaned_data['team2'])
            return HttpResponseRedirect(reverse('new:keeper'))
    else:
        form=customforms.Team()
    return render(request,'new/teams.html',{'form':form})


def keeper(request):
    arr=database.keeper_gen().generate(config.teams)
    if request.method=='POST':
        form=customforms.keeper(arr,request.POST)
        if form.is_valid():
            config.players.append(form.cleaned_data['keeper1'])
            return HttpResponseRedirect(reverse('new:batsman'))
    else:
        form=customforms.keeper(arr)
    return render(request,'new/keeper.html',{'form':form}) 


def batsman(request):
    arr=database.batsman_gen().generate(config.teams)
    if request.method=='POST':
        form=customforms.batsman(arr,request.POST)
        if form.is_valid():
            config.players.append(form.cleaned_data.get('batsman1'))
            return HttpResponseRedirect(reverse('new:allrounder'))
    else:
        form=customforms.batsman(arr)
    return render(request,'new/batsman.html',{'form':form})


def allrounder(request):
    arr=database.allrounder_gen().generate(config.teams)
    if request.method=='POST':
        form=customforms.allrounder(arr,request.POST)
        if form.is_valid():
            config.players.append(form.cleaned_data.get('allrounder1'))
            return HttpResponseRedirect(reverse('new:bowler'))
    else:
        form=customforms.allrounder(arr)
    return render(request,'new/allrounder.html',{'form':form})


def bowler(request):
    arr=database.bowler_gen().generate(config.teams)
    if request.method=='POST':
        form=customforms.bowler(arr,request.POST)
        if form.is_valid():
            config.players.append(form.cleaned_data.get('bowler1'))
            return HttpResponseRedirect(reverse('new:finalscore'))
    else:
        form=customforms.bowler(arr)
    return render(request,'new/bowler.html',{'form':form})


def finalscore(request):
    finalteam=[]
    for i in range(len(config.players)):
        for j in config.players[i]:
            finalteam.append(j)
    Myteam=config.genereateMyteam()
    percent=config.percentcalculate(Myteam)
    return render(request,'new/finalscore.html',{'team':finalteam,'percent':percent})
