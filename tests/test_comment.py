import unittest
from app.models import Blog, Comment, User
from app import db

class CommentTest(unittest.TestCase):
    def setUp(self):
        self.new_comment = Comment(id= 1,comment='test comment',user=self.username,blog_id = self.new_blog)


    def tearDown(self):
        User.query.delete()
        Blog.query.delete()

    def test_check_instance(self):
        self.assertEquals(self.new_comment.comment,'test comment')
        self.assertEquals(self.new_comment.user ,self.username)
        self.assertEquals(self.new_comment.blog_id,self.new_blog)    

class CommentTest(unittest.TestCase):
    def setUp(self):
        self.user_albert = User(username= 'albert',email='albert@yahoo.com',password = 'albert')
        self.new_blog = Blog(id=1,title='test',content='a test blog',user_id=self.user_albert)
        self.new_comment= Comment(id=1,comment='test comment',blog_id=self.new_blog.id,user_id=self.user_albert)

    def tearDown(self):
        User.query.delete()
        Comment.query.delete()
        Blog.query.delete()
        
    def test_check_instance(self):
        self.assertEquals(self.new_comment.comment, 'test comment')
        self.assertEquals(self.new_comment.blog_id,self.new_blog.id)
        self.assertEquals(self.new_comment.user_id,self.user_albert)

    def save_comment(self):
        self.new_comment.save_comment()
        self.assertTrue(len(Comment.query.all()> 0)

    def test_get_comment(self):
        self.new_comment.save_comment()
        g_comment = Comment.get_comment(1)
        self.assertTrue(g_comment is not None)