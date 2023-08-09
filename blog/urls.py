from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('search/<str:q>/', views.PostSearch.as_view()),
    path('<int:pk>/', views.PostDetail.as_view()),
    path('', views.PostList.as_view()),
    path('category/<str:slug>/', views.category_page),
    path('<int:pk>/new_comment/', views.new_comment),
    path('<int:post_id>/create_recomment/<int:comment_pk>/', views.create_recomment),
    # path('<int:pk>/new_recomment/', views.new_recomment),
    path('tag/<str:slug>/', views.tag_page),
    path('create_post/', views.PostCreate.as_view()),
    path('update_post/<int:pk>/', views.PostUpdate.as_view()),
    path('update_comment/<int:pk>/', views.CommentUpdate.as_view()),
    path('delete_comment/<int:pk>/', views.delete_comment),
    path('delete_recomment/<int:pk>/', views.delete_recomment),
    path('delete_post/<int:pk>/', views.delete_post),
    path('likes/<int:pk>/' ,views.likes,name='likes'),
    path('comment_likes/<int:pk>/' ,views.comment_likes,name='likes'),
]