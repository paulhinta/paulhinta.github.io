from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.index, name='index'),
    #path('video_stream', views.video_stream, name='video_stream'),
    path('about', views.about, name='about'),
]

urlpatterns += staticfiles_urlpatterns()