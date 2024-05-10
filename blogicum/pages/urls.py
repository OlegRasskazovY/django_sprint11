# Импорты из стандартной библиотеки
from django.urls import path

# Импорты проекта
from . import views

app_name = 'pages'

urlpatterns = [
    path('about/', views.about, name='about'),
    path('rules/', views.rules, name='rules'),
]
