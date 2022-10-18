from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post
from .forms import PostForm



def index(request):
    #IF the method is POST
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        #If the form is valid
        if form.is_valid():
            #yes save
            form.save()
            #Redirect to home
            return HttpResponseRedirect('/')
        else:
            #No, Show error
            return HttpResponseRedirect(form.erros.as_json())


    #get all post limit 20
    post = Post.objects.all().order_by('-created_at')[:20]

    return render(request, 'post.html', 
                   {'post':post})


def delete(request, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()
    return HttpResponseRedirect('/')

def edit(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect(form.errors.as_json())
    form = PostForm
    return render(request, 'edit.html', {'post': post, 'form': form})
def like(request, post_id):
    post = Post.objects.get(id=post_id)
    if post.like_count == 0:
        post.like_count += 1
        post.save()
    else:
        post.like_count = 0
        post.save()
    return HttpResponseRedirect('/')


def cancel(request, post_id):
    return HttpResponseRedirect('/')
