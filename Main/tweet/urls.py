
# from django.urls import path
# from django.conf import settings
# from django.conf.urls.static import static
# from . import views

# urlpatterns = [
#     path('',views.tweet_list, name="home"),
#     path('create/',views.tweet_create, name="home"),
#     path('<int:tweet_id>/delete/',views.tweet_delete, name="home"),
#     path('<int:tweet_id>/edit/',views.tweet_edit, name="home"),
#     path('',views.tweet_list, name="home"),
#     path('',views.tweet_list, name="home"),

# ]


from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('tweets/', views.tweet_list, name='tweet_list'),
    path('create/', views.tweet_create, name='tweet_create'),
    path('<int:tweet_id>/edit/', views.tweet_edit, name='tweet_edit'),
    path('tweets/<int:tweet_id>/delete/', views.tweet_delete, name='tweet_delete'),
    path('register/', views.register, name='register'),
    path('search/', views.tweet_search, name='search'),

]

