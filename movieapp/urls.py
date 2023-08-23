
from django.urls import path, include
from . import views
app_name='movieapp'
urlpatterns = [

    path('',views.index,name='index'),
    path('Movie/<int:movie_id>/',views.detail,name='detail'),
    path('add/',views.add_movie,name='add_movie'),
    path('update/<int:id>/',views.update_movies,name='update_movies'),
    path('delete/<int:id>/',views.delete_func,name='delete_func'),
]