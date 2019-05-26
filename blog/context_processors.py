from .models import Post

def get_latest_posts(request):
    return {'latest_posts': Post.get_latest_posts(3)}