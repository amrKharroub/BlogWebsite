import factory
from django.contrib.auth.models import User
from blog.models import Post

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
        
    username = "testuser"
    password = "testpass"
    is_superuser = True
    is_staff = True
    
    
class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Post
        
    title = "whocares"
    subtitle = "idk"
    slug = "testblog"
    author = factory.SubFactory(UserFactory)
    content = factory.Faker("text")
    published = True