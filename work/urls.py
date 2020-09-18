from django.urls import path, include
from . import views
urlpatterns = [     
    path("",views.index),
    path("account",views.profile),
    path("update_account",views.profile),
    path("add",views.noteDeal),
    path("show",views.noteDeal),
    path("list",views.noteDeal),
    
    path("pub_talking",views.talkingDeal),
    path("list_talking",views.talkingDeal),
]
