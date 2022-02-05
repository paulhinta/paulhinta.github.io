from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Gwyneth Paltrow flexes her Bitcoin knowledge as famed movie star and esteemed 'Goop' owner trumps the bald-headed Jeffrey Bezos in all-out Cryptocurrency war.")