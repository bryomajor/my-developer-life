from . import db
from sqlachemy.sql import func
from . import login_manager
from flask_login import UserMixin, current_user
from werkzeug.security import generate_password_hash, check_password_hash

@login_manager.user _loader
def load_user(user_id):
    return User.query.get(int(user_id))
    
class User(UserMixin, db.Model):

    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255), unique = True, index = True)
    pass_secure = db.Column(db.String(255))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.pass_secure, password)

    def __repr__(self):
        return f'{self.username}'


class BlogPost(db.Model):

    __tablename__ = 'blogposts'
    id = db.Column(db.Integer, primary_key = True)
    owner_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable = False)
    description = db.Column(db.String(), index = True)
    title = db.Column(db.String())
    
    @classmethod
    def get_blogposts(cls, id):
        blogposts = BlogPost.query.order_by(blogpost_id=id).desc().all()
        return blogposts

    def __repr__(self):
        return f'BlogPost {self.description}'