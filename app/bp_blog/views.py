# Import flask dependencies
from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for, jsonify

from app import db, app
from models import Post, PostSchema

bp = Blueprint(name='blog', import_name=__name__, url_prefix='/blog',
                      static_folder='static', template_folder='templates')

@bp.route('/', methods=['GET'])
def index():
    older_url="%spage/%d/" % (url_for("blog.index"), 2)
    return render_template(bp.name + "/index.html", older_url=older_url)

@bp.route('/page/<int:page_num>/', methods=['GET'])
def page(page_num):
    if page_num <= 0:
        return redirect(url_for("blog.index"))
    elif page_num == 2:
        newer_url=url_for("blog.index")
    else:
        newer_url="%spage/%d/" % (url_for("blog.index"), page_num - 1)
    older_url="%spage/%d/" % (url_for("blog.index"), page_num + 1)
    return render_template(bp.name + "/index.html", newer_url=newer_url, older_url=older_url)

@bp.route("/<int:year>/<string:name>/", methods=['GET'])
def post(year, name):
    testfile = "%s/blog/2015/test-post.json" % app.config["TEST_DATA_DIR"]
    f = open(testfile)
    teststr = f.read()
    print teststr
    post_schema = PostSchema()
    post = post_schema.loads(teststr).data;
    #return post_schema.jsonify(post)
    #return "Year=%d Name=%s" % (year, name)
    return render_template(bp.name + "/single_post.html", post=post)
