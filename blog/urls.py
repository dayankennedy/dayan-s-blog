
from django.urls import path
from .import views 
from .models import Post

app_name='blog'


urlpatterns = [
    path('', views.homepageView.as_view(), name='home'),
    path('about/', views.aboutView.as_view(), name='about'),
    path('post/', views.PostListView.as_view(), name='post'),
    path('detail/<int:pk>', views.PostDetailView.as_view(), name='detail'),
]