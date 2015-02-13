from django.test import TestCase
from models import Post

class PostTests(TestCase):

    def test_str(self):
        my_title = Post(title='This is a basic title')
        self.assertEquals(
            str(my_title), "This is a basic title",
            )

        