from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import Required, Email, EqualTo
from wtforms import ValidationError

class BlogPostForm(FlaskForm):
    title = StringField('Title', validators = [Required()])
    description = TextAreaField("Enter Blog Content", validators = [Required()])
    submit = SubmitField('Submit')


class CommentForm(FlaskForm):
    description = TextAreaField('Add Comments', validators = [Required()])
    submit = SubmitField('Submit')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.', validators = [Required()])
    submit = SubmitField('Submit')