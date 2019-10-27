from flask import render_template, request, redirect, url_for, abort, flash
from . import main
from flask_login import login_required, current_user
from ..models import BlogPost, User, Comment
from .forms import BlogPostForm, CommentForm
from flask.views import View, MethodView
from .. import db

@main.route('/')
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