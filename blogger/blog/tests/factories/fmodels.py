import factory
from django.contrib.auth.models import User
from blog.models import Post
from faker import Faker

FAKE = Faker()


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
    factory.faker.Faker

    @factory.lazy_attribute
    def content(self):
        x = ""
        for _ in range(5):
            x += FAKE.paragraph(nb_sentences=30) + "\n"
        return x

    published = True

    # I have no idea what it means
    @factory.post_generation
    def tags(self, create, extended, **kwargs):
        if not create:
            return None
        if extended:
            self.tags.add(*extended)
        else:
            self.tags.add("python", "web development", "htmx", "ML", "Back-End")
