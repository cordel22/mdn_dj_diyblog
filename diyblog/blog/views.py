from django.shortcuts import render

# Create your views here.

#   from .models import Book, Author, BookInstance, Genre
from .models import Post, Author, Comment, Topic

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_post = Post.objects.all().count()
    #   num_instances = BookInstance.objects.all().count()
    num_comments = Comment.objects.all().count()

    # Available books (status = 'a')
    #   num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    

    # The 'all()' is implied by default.
    num_authors = Author.objects.count()
    

    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    '''
    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
    }
    '''
    
    context = {
        'num_post': num_post,
        'num_comments': num_comments,
        
        'num_authors': num_authors,
        'num_visits': num_visits,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)


from django.views import generic

class PostListView(generic.ListView):
    model = Post
    paginate_by = 2
    
    context_object_name = 'post_list'   # your own name for the list as a template variable
    #   queryset = Post.objects.filter(name__icontains='blog')[:5] # Get 5 posts containing the title war
    queryset = Post.objects.all()
    #   template_name = 'posts/my_arbitrary_template_name_list.html'  # Specify your own template name/location
    template_name = 'blog/blog_list.html'

class PostDetailView(generic.DetailView):
    model = Post
    
    context_object_name = 'post_detail'   
    template_name = 'blog/blog_detail.html'
    #   https://djangocentral.com/creating-comments-system-with-django/
    '''
    if request.method == 'POST':
        post_form = CreatePostForm(data=request.POST)
        if post_form.is_valid():

            # Create Comment object but don't save to database yet
            new_post = post_form.save(commit=False)
            # Assign the current post to the comment
            #   new_comment.post = post
            # Save the comment to the database
            new_post.save()
    else:
        post_form = CreatePostForm()

    return render(request, template_name, {
                                           'new_post': new_post,
                                           'post_form': post_form})
    '''


class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 2
    
    context_object_name = 'author_list'   # your own name for the list as a template variable
    #   queryset = Post.objects.filter(name__icontains='blog')[:5] # Get 5 posts containing the title war
    queryset = Author.objects.all()
    #   template_name = 'posts/my_arbitrary_template_name_list.html'  # Specify your own template name/location
    template_name = 'blog/blogger_list.html'

class AuthorDetailView(generic.DetailView):
    model = Author
    
    context_object_name = 'author_detail'   
    template_name = 'blog/blogger_detail.html'


from django.contrib.auth.mixins import LoginRequiredMixin

class CommentedPostsByUserListView(LoginRequiredMixin,generic.ListView):
    """Generic class-based view listing Posts commented by current user."""
    model = Comment
    template_name ='blog/comment_list_posts_user.html'
    paginate_by = 5

    #   def get_queryset(self):
    #       return BookInstance.objects.filter(borrower=self.request.user).filter(status__exact='o').order_by('due_back')
    
    #   doesnt work because trolls !== users
    def get_queryset(self):
        return Comment.objects.filter(troll=self.request.user).order_by('commdatetime')


import datetime

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

#   from blog.forms import CreatePostForm

def create_post_author(request, slug):

    template_name = 'create_post_author.html'
    '''
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True)
    new_comment = None
    '''
    # Comment posted
    '''
    if request.method == 'POST':
        post_form = CreatePostForm(data=request.POST)
        if post_form.is_valid():

            # Create Comment object but don't save to database yet
            new_post = post_form.save(commit=False)
            # Assign the current post to the comment
            #   new_comment.post = post
            # Save the comment to the database
            new_post.save()
    else:
        post_form = CreatePostForm()

    return render(request, template_name, {
                                           'new_post': new_post,
                                           'post_form': post_form})
    '''
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView                                           

'''
class PostCreateView(CreateView):
    model = Post
    fields = ['name', 'author', 'content', 'topic']
'''

from django.template.loader import render_to_string

class PostCreate(CreateView):
    model = Post
    fields = '__all__'
    success_url = reverse_lazy('blogs')


class CommentCreate(CreateView):
    model = Comment
    fields = '__all__'
    success_url = reverse_lazy('blogs')





















