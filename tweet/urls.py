from django.urls import path

from . import views
from .views import TweetListView, TweetDetailView, TweetCreateView, TweetUpdateView, TweetDeleteView

urlpatterns = [
    path('', TweetListView.as_view(), name='tweet-home'),
    path('tweet/<int:pk>', TweetDetailView.as_view(), name='tweet-detail'),
    path('tweet/new/', TweetCreateView.as_view(), name='tweet-create'),
    path('tweet/<int:pk>/update/', TweetUpdateView.as_view(), name='tweet-update'),
    path('tweet/<int:pk>/delete', TweetDeleteView.as_view(), name='tweet-delete')
]