from django.test import TestCase
from blog.tests.factories.fmodels import PostFactory


class TestPostModel(TestCase):
    def setUp(self):
        self.post1 = PostFactory(title="test_title", tags=["test_tag1", "test-tag2"])

    def test_str_return(self):
        self.assertEqual(str(self.post1), "test_title")

    def test_add_tags(self):
        tags = self.post1.tags
        self.assertEqual(tags.count(), 2)
        for name in tags.names():
            self.assertIn(name, ["test_tag1", "test-tag2"])
