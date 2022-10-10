from os import name
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect,Http404
from django.urls import reverse
from .models import Author,Post,Tag,Comment,Picture
from .forms import CommentForm,picform
from django.views.generic.base import TemplateView
from django.views.generic import ListView,DetailView
from django.views.generic.edit import FormView,CreateView

# Create your views here.
def index(request):


    posts = Post.objects.all().order_by("Date")
    posts = posts[:3]




    return render(request,"blogs/index.html",{
        "posts":posts
    })



# def indpost2(request,slug):
#     li = list(postings.keys())

#     pos = li[slug - 1]

#     redirect_url = reverse("indpost",args=[pos])

#     return HttpResponseRedirect(redirect_url)

def indpost(request,slug):
    # try:
    #     pos = postings[slug]
    #     context = {
    #         "post_title":slug,
    #         "post_det":pos
    #     }
    #     return render(request,"blogs/post.html",context=context)
    # except:
    #     return Http404
    post = get_object_or_404(Post, Slug=slug)

    if request.method == "POST":
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = Comment(
                name=form.cleaned_data["name"],
                email = form.cleaned_data["email"],
                content = form.cleaned_data["content"]
            )
            comment.save()
            redirect_url = reverse("indpost",args=[slug])

            return HttpResponseRedirect(redirect_url)

    else:

        form = CommentForm()
        slugs = request.session.get("readlater")

        if slug == slugs:
            Later = True
        else:
            Later = False



    return render(request,"blogs/post.html",context={
            "post":post,
            "form":form,
            "later":Later
        })




def posts(request):

    posts = Post.objects.all().order_by("Date")
    

    return render(request,"blogs/posts2.html",{
        "posts":posts
    })

class thankyou(TemplateView):
    template_name = "blogs/thankyou.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message"] = "This works"
        return context


class allposts(ListView):
    template_name = "blogs/thankyou.html"
    model = Comment
    context_object_name = "comments"

    def get_queryset(self):
        data =  super().get_queryset()
        data.filter()
        return data

class op(FormView):
    template_name = "blogs/post.html"
    form_class = CommentForm
    success_url = "/thankyou"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class opcreate(CreateView):
    template_name = "blogs/post.html"
    form_class = CommentForm
    success_url = "/thankyou"
    model = Comment


def uplo(request):
    if request.method == "POST":
        form = picform(request.POST,request.FILES)

        if form.is_valid():
            images = Picture(pic=request.FILES["pic"])
            images.save()
            return HttpResponseRedirect("posts")

    else:
        form = picform()

    return render(request,"blogs/fileupload.html",context={
        "form":form
    })


def sess(request):
    if request.method == "POST":
        slug = request.POST["read"]
        request.session["readlater"] = slug
    
        redirect_url = reverse("indpost",args=[slug])

        return HttpResponseRedirect(redirect_url)

