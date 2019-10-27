import unittest
from app.models import BlogPost, Comment, User
from app import db

class BlogPost(unittest.TestCase):
    '''
    A test case that tests the behaviours of the BlogPost model
    '''

    def setUp(self):
        '''
        Method that will run before each test is ran
        '''
        self.new_blogpost = BlogPost(blogpost_title = "Python", blogpost_description = "Python is such a powerful language")
        self.new_comment = Comment(comment_content = "I love this", blogpost = self.new_blogpost)


    def tearDown(self):
        db.session.delete(self)
        User.query.commit()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_blogpost, BlogPost))
        self.assertTrue(isinstance(self.new_comment, Comment))

    def test_check_instance_variables(self):
        self.assertEquals(self.new_blogpost, blogpost_description, "Python is such a powerful language")
        self.assertEquals(self.new_comment.blogpost, self.new_blogpost, "I love this")