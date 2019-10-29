import unittest
from app.models  import User,Blog
from app import db

class BlogTest(unittest.TestCase):
    def setUp(self):
        self.user_brian = User(username="brian",password="brian",email="brian@yahoo.com")
        self.new_blog = Blog(id="1",title="testing",content="testing blog",user_id=self.user_brian)
    def tearDown(self):
        Blog.query.delete()
        User.query.delete()

    def test_check_instance(self):
        self.assertEquals(self.new_blog.title, 'testing')  
        self.assertEquals(self.new_blog.content, 'testing blog')   
        self.assertEquals(self.new_blog.user_id,self.user_brian)

    def test_save_blog(self):
        self.new_blog.save_blog()
        self.assertTrue(len(Blog.query.all()> 0))

    def test_get_blog(self):
        self.new_blog.save_blog()
        g_blog = Blog.get_blog(1)
        self.assertTrue(g_blog is not None)
