from . import views
from django.urls import path

app_name = 'pokerMain'
urlpatterns = [
    path('', views.index, name="index"),
    path('play/', views.play_game, name="play_game"),
    path('play/raise', views.clicked_raise, name='clicked_raise'),
    path('play/fold', views.clicked_fold, name='clicked_fold'),
    path('report/', views.report_bug, name='report_bug')



]