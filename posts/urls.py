from django.urls import path
from posts.views import *
from . import views

urlpatterns = [
    # path('', hello_world, name = 'hello_world'),
    # path('<int:id>', get_post_detail, name = "게시글 조회"),
    path('', post_list, name = "post_list"),
    path('<int:id>/', post_detail, name = "post_detail"), #POST 단일 조회
    path('<int:id>/comment', comment_list, name = "comment_list"),
    path('recent', view_recent_week, name="recent_week")
]