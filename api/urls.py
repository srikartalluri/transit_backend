from django.urls import path
from .views import PersonView, hello, GetView

urlpatterns = [
     path('home', PersonView.as_view()),
     path('', hello),
     path('get', GetView.as_view())
]
