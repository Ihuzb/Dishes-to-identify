from django.conf.urls import url
from RickAndMorty import views

urlpatterns = [
    url('^updateImg', views.updateImg)
]
