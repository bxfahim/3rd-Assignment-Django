from django.shortcuts import render, get_object_or_404
from . models import *
from .models import Post
from django.core.paginator import Paginator


from .models import Post
from .forms import CommentForm

# Create your views here.
def home_view(request):
    posts = Post.objects.all()
    header_post = Post.objects.filter(id='3')
    featured_post = Post.objects.filter(featured=True)[:4]
    story_post = Post.objects.filter(featured= False)[:3]
    popular_post = Post.objects.filter(featured=True)[:5]
    template_name = 'home.html'
    context = {'posts':posts, 'header_post':header_post, 'featured_post':featured_post, 'story_post':story_post, 'popular_post':popular_post}
    return render(request, template_name, context)


def blog_page(request):
    queryset = Post.objects.filter(post_status ='publish').order_by('-created')
    per_page = 2
    paginator = Paginator(queryset, per_page)
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)
    template_name = 'blog/blog-page.html'
    context = {'posts':posts}
    return render(request, template_name, context)


def article_view(request,slug):
    post = get_object_or_404(Post, slug=slug)
    template_name = 'article.html'
    context= {'post':post,}
    return render(request, template_name, context)


def category_page(request,category_slug):
    category_url = get_object_or_404(Category, slug=category_slug)
    posts = Post.objects.filter(category = category_url)
    template_name = 'category-page.html'
    context = {'posts':posts}
    return render(request, template_name, context)



# Creating Comments forms here 

def post_detail(request, slug):
    template_name = 'comments/post_detail.html'
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True)
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, template_name, {'post': post,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})
