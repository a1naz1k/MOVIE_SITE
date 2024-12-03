from django.contrib.auth.views import LogoutView
from django.urls import path
from .views import *


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),


    path('', MovieListViewSet.as_view({'get': 'list'}), name='movie_list'),
    path('<int:pk>/', MovieDetailViewSet.as_view({'get': 'retrieve'}), name='movie_detail'),

    path('user/', ProfileViewSet.as_view({'get': 'list'}), name='profile_list'),
    path('user/<int:pk>/', ProfileViewSet.as_view({'get': 'retrieve'}), name='profile_detail'),


    path('director/', DirectorViewSet.as_view({'get': 'list', }), name='director_list'),
    path('director/<int:pk>/', DirectorViewSet.as_view({'get': 'retrieve'}), name='director_detail'),

    path('actor/', ActorViewSet.as_view({'get': 'list'}), name='actor_list'),
    path('actor/<int:pk>/', ActorViewSet.as_view({'get': 'retrieve'}), name='actor_detail'),

    path('history/', HistoryViewSet.as_view({'get': 'list'}), name='history_list'),
    path('history/<int:pk>/', HistoryViewSet.as_view({'get': 'retrieve',
                                                      'put': 'update',
                                                      'delete': 'destroy'}), name='history_detail'),

]
