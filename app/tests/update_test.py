import unittest
from app.models import User, Post
from app import db


class PostModelTest(unittest.TestCase):

    def setUp(self):
        self . user_Ngenoh  =  User (
            username="ngenoh", password="11111", email="zefmesssi77@gmail.com")
        self.new_post = Post(
            title="blog", body="blogging website", user_id=self.user_ngenoh.id)

    def tearDown(self):
        Post.query.delete()
        User.query.delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_post, Post))

    def test_check_instance_variables(self):
        self.assertEquals(self.new_post.title, 'blog')
        self.assertEquals(self.new_post.body, "blogging website")
        self.assertEquals(self.new_post.user_id, self.user_abdi.id)

    def test_save_blog(self):
        self.new_post.save_post()
        self.assertTrue(len(Post.query.all()) > 0)

    def test_get_posts(self):

        self.new_post.save_blog()
        posts = Post.get_posts()
        self.assertTrue(len(posts) == 1