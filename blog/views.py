from django.shortcuts import render
from .models import Post


# Create your views here.
def posts(request):
    context = {
        'postss': Post.objects.all()
    }
    return render(request, 'blog/index.html', context)
