from flask import abort, Blueprint, render_template
from slugify import slugify
from searchform import SearchForm


mod_search = Blueprint('search', __name__)

rent_or_sale_dict = {
    'me-qira': 'Me qira',
    'ne-shitje': 'Ne shitje'
}

city_dict = {
    'ferizaj': {
        'name': 'Ferizaj',
        'hoods': [
            {
                'name': 'Inda hood',
                'slug': 'inda-hood',
                'geojson': ''
            }
        ]
    },
    'prishtine': {
        'name': 'Prishtine',
        'hoods': [
            {
                'name': 'Inda other hood',
                'slug': 'inda-other-hood',
                'geojson': ''
            }
        ]
    },
}

@mod_search.route('/', methods=['GET'])
def index():
    form = SearchForm()
    return render_template('mod_search/index.html', form=form)

@mod_search.route('/<city>/<rent_or_sale>', methods=['GET'])
def city_search(city, rent_or_sale):
    if city in city_dict and slugify(rent_or_sale, to_lower=True) in rent_or_sale_dict:
        return render_template('mod_search/results.html',
                               city=city_dict[city]['name'],
                               rent_or_sale=rent_or_sale_dict[rent_or_sale])
    else:
        abort(400)

