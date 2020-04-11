from django.conf.urls import url
from . import views
from django.urls import path

app_name = 'boke'
urlpatterns = [
    path('', views.home, name='home'),
    path('^post/<int:pk>/', views.pages, name='pages'),
    path('files/<int:year>/<int:month>/', views.files, name='files'),
    path('classification/<int:pk>/', views.classification, name='classification'),
    path('files/', views.files),
    url(r'^(\d+)$', views.home),
]
