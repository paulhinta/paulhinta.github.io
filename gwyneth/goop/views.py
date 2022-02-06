from gc import collect
from django.shortcuts import render
from django.http import HttpResponse

#from utils import get_db_handle

from django.shortcuts import render
from django.http.response import StreamingHttpResponse
'''
from goop.camera import VideoCamera
# Create your views here.
def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
def video_stream(request):
    return StreamingHttpResponse(gen(VideoCamera()),
                    content_type='multipart/x-mixed-replace; boundary=frame')
'''
#db = get_db_handle()

def index(request):
    #x = db.find({"listing_url":"https://www.airbnb.com/rooms/10006546"})
    
    context = {}
    #context['query'] = str(x[0])
    
    return render(request, 'home.html', context)
    #return HttpResponse(str(x[0]))
    #return HttpResponse("Gwyneth Paltrow flexes her Bitcoin knowledge as famed movie star and esteemed 'Goop' owner trumps the bald-headed Jeffrey Bezos in all-out Cryptocurrency war.")

def about(request):
    return render(request, 'about.html')