from django.contrib import admin
from django.urls import path
from . import views

app_name='new'
urlpatterns=[
    path('',views.index,name='index'),
    path('keeper',views.keeper,name='keeper'),
    path('batsman',views.batsman,name='batsman'),
    path('allrounder',views.allrounder,name='allrounder'),
    path('bowler',views.bowler,name='bowler'),
    path('finalscore',views.finalscore,name='finalscore')
    # path('disp',views.disp,name='disp')
]

