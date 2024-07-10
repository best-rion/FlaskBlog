from flask import Blueprint
from flask import render_template, request, Blueprint
from flaskblog.models import Post, Comment

main = Blueprint('main', __name__)



@main.route("/")
@main.route("/home")
def home():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.id.desc()).paginate(page=page, per_page=5)
    return render_template('home.html',posts=posts, title="Timeline")

@main.route("/about")
def about():
    return "<h1>The About Page</h1>"

