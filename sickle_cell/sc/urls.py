from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='sickle-cell-landing-page'),
    path('diagnose/', views.question_prediction, name='quest-predict'),
    path('acute/', views.acute_result, name="acute-result")
]
