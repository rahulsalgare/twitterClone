from django.urls import path

from .views import TweetListView, UserTweetListView, TweetDetailView, TweetCreateView, TweetUpdateView, TweetDeleteView, about

urlpatterns = [
    path('', TweetListView.as_view(), name='tweet-home'),
    path('user/<str:username>', UserTweetListView.as_view(), name='user-tweets'),
    path('about/', about, name='tweet-about'),
    path('tweet/<int:pk>', TweetDetailView.as_view(), name='tweet-detail'),
    path('tweet/new/', TweetCreateView.as_view(), name='tweet-create'),
    path('tweet/<int:pk>/update/', TweetUpdateView.as_view(), name='tweet-update'),
    path('tweet/<int:pk>/delete', TweetDeleteView.as_view(), name='tweet-delete')
]