from django.urls import path
from . import views


urlpatterns = [
    path("",views.index,name="index"),
    path("posts",views.posts,name="posts"),
    path("posts/<slug:slug>",views.indpost,name="indpost"),
    path("files",views.uplo,name="uplo"),
    path("session",views.sess,name="sess"),
    
]


