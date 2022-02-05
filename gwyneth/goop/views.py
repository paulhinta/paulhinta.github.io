from gc import collect
from django.shortcuts import render
from django.http import HttpResponse

from utils import get_db_handle

db = get_db_handle()

def index(request):
    x = db.find({"listing_url":"https://www.airbnb.com/rooms/10006546"})
    
    context = {}
    context['query'] = str(x[0])
    
    return render(request, 'home.html', context)
    #return HttpResponse(str(x[0]))
    #return HttpResponse("Gwyneth Paltrow flexes her Bitcoin knowledge as famed movie star and esteemed 'Goop' owner trumps the bald-headed Jeffrey Bezos in all-out Cryptocurrency war.")