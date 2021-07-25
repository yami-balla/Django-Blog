from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    Status_Choices =(
        ('Published', 'Published'),
        ('Draft', 'Draft'),
    )
    Title = models.CharField(max_length=100)
    Slug = models.SlugField(unique=True)
    Author = models.ForeignKey(User, null=True, blank=True, on_delete=CASCADE)
    Updated_on = models.DateTimeField(auto_now=True)
    Content = models.TextField()
    Created_on = models.DateTimeField(auto_now_add=True)
    Status = models.CharField(max_length=10, default='Draft', choices=Status_Choices)
