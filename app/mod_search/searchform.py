# coding=utf-8
from wtforms import Form, SelectField, SelectMultipleField

class SearchForm(Form):

    '''
    def __init__(self, **kwargs):
        for price in range(100, 1000, 50):
            self.price_from_rental.choices.append({
                (price, str(price))
            })

            self.price_to_rental.choices.append({
                (price, str(price))
            })


        for price in range(5000, 300000, 5000):
            self.price_from_sale.choices.append({
                (price, str(price))
            })

            self.price_to_sale.choices.append({
                (price, str(price))
            })
    '''

    sale_or_rent = SelectField('Me qira / Ne shitje',
        choices=[
            ('me-qira','Me qira'), # sale
            ('ne-shitje','Ne shitje') # rent
        ],
        default='ne-shitje')

    municipalities = SelectField('Komuna',
        choices=[
            ('ferizaj','Ferizaj'),
            ('prishrine','Prishtinë')
        ],
        default='ferizaj')

    cities = SelectField('Cities',
        choices=[
            ('all','All'),
            ('ferizaj','Ferizaj'),
            ('prishrine','Prishtinë')
        ],
        default='all')

    type = SelectField('Type',
        choices=[
            ('any-type','Any type'),
            ('apartment','Apartment'),
            ('house','House')
        ],
        default='any-type')

    price_from_rental = SelectField('Price from', choices=[('all', 'All')])
    price_to_rental = SelectField('Price to', choices=[('all', 'All')])

    price_from_sale = SelectField('Price from', choices=[('all', 'All')])
    price_to_sale = SelectField('Price to', choices=[('all', 'All')])

    bedrooms = SelectField('Bedrooms',
        choices=[
            ('any-beds','Any beds'), # Any bedroom
            ('studio','Studio'), # Studio
            ('1-bedroom','1 Bedroom'), # 1 bedroom
            ('2-bedroom','2 Bedroom'), # 2 bedroom
            ('3-bedroom','3 Bedroom'), # 3 bedroom
            ('4-bedroom','4 Bedroom'), # 4 bedroom
            ('5-bedroom','5+ Bedroom') # 5 bedroom
        ],
        default='any-type')

    bathrooms = SelectField('Bathrooms',
        choices=[
            ('any-baths','Any baths'),
            ('1-bathroom','1 Bathroom'), # 1 bedroom
            ('2-bathroom','2 Bathroom'), # 2 bedroom
            ('3-bathroom','3 Bathroom'), # 3 bedroom
            ('4-bathroom','4 Bathroom'), # 4 bathroom
        ],
        default='any-baths')

    #range(start, stop, step)