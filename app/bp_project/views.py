# Import flask dependencies
from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for

from app import db
from models import Project

bp = Blueprint(name='project', import_name=__name__, url_prefix='/project',
                      static_folder='static', template_folder='templates')

@bp.route('/', methods=['GET'])
def index():
    projects = Project.query.order_by(Project.priority).all();
    return render_template(bp.name + "/index.html", projects=projects)

@bp.route("/<string:id>/", methods=['GET'])
def project(id):
    project = Project.query.get(id);
    if (project is None):
        return redirect(url_for(bp.name + ".index"))
    return render_template(bp.name + "/" + project.id + "/index.html", project=project)
