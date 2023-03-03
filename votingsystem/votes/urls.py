from django.urls import path
from .views import index, detail, result

app_name = "votes"

urlpatterns = [
    path('index/', index, name="index"),
    path('<int:pk>/', detail, name='detail'),
    path('<int:pk>/result/', result, name='result'),

]
