from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('<slug:slug>/', views.post_detail, name='post_detail')
    #path('', views.TabelView.as_view(), name='tabel')
    #path('', views.IndexView, name='polls')
]