# Import flask dependencies
from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for

from app import db
from forms import RegistrationForm
from models import User

bp = Blueprint(name='register', import_name=__name__, url_prefix='/register',
                      static_folder='static', template_folder='templates')

@bp.route('/', methods=['GET', 'POST'])
def index():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User(username=form.username.data,
                    email=form.email.data)
        # don't store password to keep example simple
        #            password=form.password.data)
        db.session.add(user)
        flash('Thanks for registering')
        return redirect(url_for('root.index'))
        #return redirect(url_for('login'))
    return render_template(bp.name + '/index.html', form=form)
