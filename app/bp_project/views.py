# Import flask dependencies
from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for, jsonify, Response, json

from app import db
from models import Project, ProjectSchema

bp = Blueprint(name='project', import_name=__name__, url_prefix='/project')

"""
@bp.route('/', methods=['GET'])
def index():
    projects = Project.query.order_by(Project.priority).all();
    return render_template(bp
.name + "/index.html", projects=projects)

@bp.route("/<string:id>/", methods=['GET'])
def project(id):
    project = Project.query.get(id);
    if (project is None):
        return redirect(url_for(bp.name + ".index"))
    return render_template(bp.name + "/" + project.id + "/index.html", project=project)
"""

@bp.route('/', methods=['GET'])
def index():
    projects = Project.query.order_by(Project.priority).all()
    result = ProjectSchema(many=True).dump(projects)
    # return jsonify(projects=result.data)
    return Response(json.dumps(result.data),  mimetype='application/json')


@bp.route("/<string:id>/", methods=['GET'])
def project(id):
    project = Project.query.get(id)
    if project is None:
        pass
    return ProjectSchema().jsonify(project)
