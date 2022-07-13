from django.db import models

# Create your models here.

class Topic(models.Model):
    """Model representing a topic of a blog genre."""
    name = models.CharField(max_length=200, help_text='Enter a blog topic (e.g. Big Naturals)')

    def __str__(self):
        """String for representing the Model object."""
        return self.name
        
    def display_topic(self):
        """Create a string for the Topic. This is required to display Topic in Admin."""
        return ', '.join(topic.name for topic in self.topic.all()[:3])

    display_topic.short_description = 'Topic'
        
        
from django.urls import reverse # Used to generate URLs by reversing the URL patterns

class Post(models.Model):
    """Model representing a blog Post (but not a Comment)."""
    #   title = models.CharField(max_length=200)
    name = models.CharField(max_length=200)

    # Foreign Key used because blog Post can only have one Author, but Author s can have multiple blog Posts
    # Author as a string rather than object because it hasn't been declared yet in the file
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)

    #   summary = models.TextField(max_length=1000, help_text='Enter a brief description of the book')
    content = models.TextField(max_length=1000, help_text='Enter the blog Post content')
    #   isbn = models.CharField('ISBN', max_length=13, unique=True,
    #                            help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')

    # ManyToManyField used because Topic can contain many books. Topics can cover many genres.
    # Topic class has already been defined so we can specify the object above.
    #   genre = models.ManyToManyField(Genre, help_text='Select a genre for this book')
    topic = models.ManyToManyField(Topic, help_text='Select a Topic for this blog Post')
    
    pubdatetime = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        """String for representing the Model object."""
        return self.name

    def get_absolute_url(self):
        """Returns the URL to access a detail record for this blog Post, like with comments maybe?."""
        return reverse('post-detail', args=[str(self.id)])
        
        
    class Meta:
        ordering = ['name', '-pubdatetime']
        

import uuid # Required for unique Comment instance

#   class BookInstance(models.Model):
class Comment(models.Model):
    """Model representing a specific copy of a book (i.e. that can be borrowed from the library)."""
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particular book across whole library')
    # book = models.ForeignKey('Book', on_delete=models.RESTRICT, null=True)
    # imprint = models.CharField(max_length=200)
    # due_back = models.DateField(null=True, blank=True)

    """Model representing a specific Comment of a blog."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particular Comment across whole blog')
    post = models.ForeignKey('Post', on_delete=models.RESTRICT, null=True)
    
    # Foreign Key used because Comment can only have one Troll, but Troll s can have multiple blog Posts Comment s
    # Troll as a string rather than object because it hasn't been declared yet in the file
    troll = models.ForeignKey('Troll', on_delete=models.SET_NULL, null=True)
    
    content = models.TextField(max_length=1000, help_text='Enter the blog Post content')
    
    commdatetime = models.DateTimeField(auto_now=True)
    
    # LOAN_STATUS = (
        # ('m', 'Maintenance'),
        # ('o', 'On loan'),
        # ('a', 'Available'),
        # ('r', 'Reserved'),
    # )

    # status = models.CharField(
        # max_length=1,
        # choices=LOAN_STATUS,
        # blank=True,
        # default='m',
        # help_text='Book availability',
    # )

    class Meta:
        ordering = ['-commdatetime']

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.id} ({self.post.name})'



class Author(models.Model):
    """Model representing an author."""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    

    class Meta:
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        """Returns the URL to access a particular Author instance."""
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.last_name}, {self.first_name}'


class Troll(models.Model):
    """Model representing an author."""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    

    class Meta:
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        """Returns the URL to access a particular Troll instance."""
        return reverse('troll-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.last_name}, {self.first_name}'



