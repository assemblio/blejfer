from flask import Blueprint, render_template
from realestate_entryform import RealEstateEntryForm

mod_admin = Blueprint('admin', __name__, url_prefix='/admin')

@mod_admin.route('/', methods=['GET'])
def index():
    form = RealEstateEntryForm()
    return render_template('mod_admin/index.html', form=form)
