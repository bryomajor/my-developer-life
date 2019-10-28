from flask import render_template, request, redirect, url_for, abort, flash
from . import main
from flask_login import login_required, current_user
from ..models import BlogPost, User, Comment
from .forms import BlogPostForm, CommentForm, UpdateProfile
from flask.views import View, MethodView
from .. import db, photos

@main.route('/', methods = ['GET', 'POST'])
def index():
    '''
    View function that returns the index page and it's data
    '''
    title = "Brian's Blog"
    intro = "Welcome to My Developer Journey"
    blogpost = BlogPost.query.filter_by().first()

    return render_template('index.html', title = title, intro = intro, blogpost = blogpost)

@main.route('/blogposts/new', methods = ['GET', 'POST'])
@login_required
def new_blogpost():
    form = BlogPostForm()
    if form.validate_on_submit():
        description = form.description.data
        title = form.title.data
        owner_id = current_user
        date = date.now
        new_blogpost = BlogPost(owner_id = current_user._get_current_object().id, title = title, description = description)
        db.session.add(new_blogpost)
        db.session.commit()

        return redirect(url_for('main.index'))

    return render_template('blogposts.html', form = form)

@main.route('/comment/new/<int:blogpost_id>', methods = ['GET', 'POST'])
@login_required
def new_comment(blogpost_id):
    form = CommentForm()
    blogpost = BlogPost.query.get(blogpost_id)
    if form.validate_on_submit():
        description = form.description.data

        new_comment = Comment(description = description, user_id = current_user._get_current_object().id, blogpost_id = blogpost_id)
        db.session.add(new_comment)
        db.session.commit()

        return redirect(url_for('.new_comment', blogpost_id = blogpost_id))

    all_comments = Comment.query.filter_by(blogpost_id = blogpost_id).all()

    return render_template('comments.html', form = form, comment = all_comments, blogpost = blogpost)

@main.route('/about')
def about():
    '''
    View function that returns the about page
    '''
    return render_template('about.html')

@main.route('/contact')
def contact():
    '''
    View function that returns the contact page
    '''
    return render_template('contact.html')

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template('profile/profile.html', user = user)

@main.route('/user/<uname>/update', methods = ['GET', 'POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile', uname=user.username))

    return render_template('profile/update.html', form = form)

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))