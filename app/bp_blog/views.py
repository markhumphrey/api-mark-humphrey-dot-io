# Import flask dependencies
from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for, jsonify

from app import db, app
from models import Post, PostSchema

bp = Blueprint(name='blog', import_name=__name__, url_prefix='/blog',
                      static_folder='static', template_folder='templates')

POSTS_PER_PAGE = 10;

def _page(page_num):
    pagination = Post.query.order_by(Post.date.desc()).paginate(page=page_num, per_page=POSTS_PER_PAGE, error_out=True)
    if pagination.has_next:
        older_url="%spage/%d/" % (url_for("blog.index"), page_num + 1)
    else:
        older_url=None

    if page_num <= 1:
        newer_url=None
    elif page_num == 2:
        newer_url=url_for("blog.index")
    else:
        newer_url="%spage/%d/" % (url_for("blog.index"), page_num - 1)

    return render_template(bp.name + "/index.html", posts=pagination.items, newer_url=newer_url, older_url=older_url)

@bp.route('/', methods=['GET'])
def index():
    return _page(1)

@bp.route('/page/<int:page_num>/', methods=['GET'])
def page(page_num):
    if page_num <= 0:
        return redirect(url_for("blog.index"))
    return _page(page_num)

@bp.route("/<int:year>/<int:month>/<string:name>/", methods=['GET'])
def post(year, month,  name):
    post = Post.query.filter(Post.date.between("%d-%d-01" % (year, month),
                                               "%d-%d-31" % (year, month)),
                             Post.uri==name).first()
    if (post is None):
        return redirect(url_for("blog.index"))
    return render_template(bp.name + "/single_post.html", post=post)
