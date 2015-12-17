from flask import Blueprint

mod_admin = Blueprint('admin', __name__, url_prefix='/admin')

@mod_admin.route('/', methods=['GET'])
def index():
    return 'TODO: admin'
