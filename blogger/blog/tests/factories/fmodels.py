import factory
from django.contrib.auth.models import User
from blog.models import Post


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker("name")
    password = "test_password123"
    is_superuser = True
    is_staff = True


class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Post

    title = factory.Faker("sentence", nb_words=12)
    subtitle = factory.Faker("sentence", nb_words=7)
    slug = factory.Faker("slug")
    author = factory.SubFactory(UserFactory)

    def content(self):
        x = ""
        FAKER = factory.Faker()
        for _ in range(5):
            x += FAKER.paragraph(sentences=30) + "\n"
        return x

    published = True
