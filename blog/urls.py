from django.urls import path
import pdb;

from . import views

urlpatterns = [
    path("", views.StartingPageView.as_view(), name="starting-page"),
    # path("", views.starting_page, name="starting-page"),
    # pdb.set_trace(),
    path("posts", views.AllPostView.as_view(), name="posts-page"),
    # path("posts", views.posts, name="posts-page"),
    path("posts/<slug:slug>", views.SinglePostView.as_view(), 
        name="post-detail-page"), #/posts/my-first-post
    # path("posts/<slug:slug>", views.post_detail, 
    #     name="post-detail-page") #/posts/my-first-post
    path("read-later", views.ReadLaterView.as_view(), name="read-later")
]