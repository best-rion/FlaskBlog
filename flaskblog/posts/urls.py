from flask import Blueprint
from flask import (render_template, url_for, flash,
                   redirect, request, abort, Blueprint)
from flask_login import current_user, login_required
from flaskblog import db
from flaskblog.models import Post, Comment
from flaskblog.posts.forms import PostForm
from flaskblog.comments.forms import CommentForm
posts = Blueprint('posts', __name__)


@posts.route("/post/new", methods=['GET', 'POST'])
@login_required # ekhan theke {{ current_user }} 'account.html'e jachhe
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, content=form.content.data, author=current_user)
        db.session.add(post)
        db.session.commit()

        flash('Your Post has been created', 'success')
        return redirect(url_for('main.home'))
    return render_template('create_post.html', title='New Post', form=form)

@posts.route("/post/<int:post_id>", methods=['GET', 'POST'])
def one_post(post_id):
    post = Post.query.get_or_404(post_id)
    comments = Comment.query.filter_by(origin_post=post)
    comment_form = CommentForm()

    if comment_form.validate_on_submit():
        new_comment = Comment(content=comment_form.content.data, author=current_user, origin_post=post)
        post.latest_comment = new_comment.id
        db.session.add(new_comment)
        db.session.commit()

        comment_form.content.data = None
        flash('Comment posted !', 'success')

        # return redirect(url_for('posts.one_post', post_id=post.id))

    return render_template('post.html', title=post.title, post=post, comments=comments, comment_form=comment_form)


@posts.route("/post/<int:post_id>/update", methods=['GET', 'POST'])
@login_required 
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    form = PostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()
        flash('Post has been updated', 'success')
        return redirect(url_for('posts.one_post', post_id=post.id))
    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content

    return render_template('create_post.html', title='Update Post', form=form)

@posts.route("/post/<int:post_id>/delete", methods=['POST'])
@login_required 
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash('Post deleted successfully', 'success')
    return redirect(url_for('main.home'))



