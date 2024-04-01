from django.shortcuts import render,HttpResponse, get_object_or_404,redirect
from .models import Post
from .forms import PostForm
from django.contrib import messages

def post_index(request):
    posts = Post.objects.all()
    return render(request, "post/index.html", {'posts': posts})


def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    context = {
        'post': post
    }
    return render(request, "post/detail.html", context)


def post_create(request):
    # if request.method == "POST":
    #     print(request.POST)
    #
    # title = request.POST.get("title")
    # content = request.POST.get("metin")
    # Post.objects.create(title=title, content=content)

    # if request.method == "POST":
    #     # Formdan gelen bilgileri kaydet
    #     form = PostForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    # else:
    #     # Formu kullanıcıya göster
    #     form = PostForm()

    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            # Yeni postun detay sayfasına yönlendirme yap
            messages.success(request, "Başarılı bir şekilde oluşturdunuz", extra_tags='message-succes')

            return redirect('post:detail', id=post.id)
    else:
        form = PostForm()
    
    return render(request, "post/form.html", {'form': form})


def post_update(request, id):
    post = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None, instance=post)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, "Başarılı bir şekilde güncellediniz",extra_tags='message-update-succes')
            # Güncelleme işlemi tamamlandıktan sonra detay sayfasına yönlendirme yap
            return redirect('post:detail', id=post.id)
    
    context = {
        'form': form
    }

    return render(request, "post/form.html", context)

def post_delete(request, id):
    post = get_object_or_404(Post, id=id)
    post.delete()
    messages.success(request, "Başarılı bir şekilde silme işlemini gerçekleştirdiniz.",extra_tags='message-deleted-succes')
    return redirect('post:index')