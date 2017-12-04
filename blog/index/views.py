from datetime import datetime, timedelta
from django.shortcuts import render
from posts.models import Post


# Create your views here.
def index(request):
    recent_posts = []
    a = Post()
    a.text = 'Post text goes here'
    a.title = 'Post title goes here'
    a.creation_date = datetime.now()  # comment
    recent_posts.append(a)
    b = Post()
    b.title = 'Older title'
    b.text = 'Older text'
    b.creation_date = datetime.now() - timedelta(days=1)
    recent_posts.append(b)
    return render(request, 'index/index.html', {'posts': recent_posts})
