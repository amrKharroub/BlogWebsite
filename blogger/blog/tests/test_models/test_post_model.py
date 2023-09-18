from django.test import TestCase
from blog.tests.factories.fmodels import PostFactory

class TestPostModel(TestCase):
    def setUp(self):
        self.post1 = PostFactory(title="test_title")
    
    def test_str_return(self):
        self.assertEqual(str(self.post1), "test_title")