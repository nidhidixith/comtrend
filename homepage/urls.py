from django.urls import path
from . import views
urlpatterns = [
    path('',views.firstview),
    path('firstpage.html',views.indians,name='indians'),
    path('firstpage.html',views.indians,name='americans'),
    path('firstpage.html',views.indians,name='kids'),
    path('firstpage.html',views.indians,name='classics'),
    path('firstpage.html',views.indians,name='mostviewed'),
    path('firstpage.html',views.indians,name='short'),
    path('firstpage.html',views.indians,name='medium'),
    path('firstpage.html',views.indians,name='long')



]

