from django.urls import path
from . import views

app_name = 'firstapp'

urlpatterns = [
    path('', views.blog ),
    # views.py의 blog 함수로 연결
    path('predictP', views.blog2),
    # views.py의 blog2 함수로 연결
    path('predictP.', views.blog3, name = 'PredictP.'),
    path('predictP..', views.blog4, name = 'PredictP..'),
    path('predictP...', views.blog5, name = 'PredictP...'),
    path('csv_model/', views.csv_model)
]