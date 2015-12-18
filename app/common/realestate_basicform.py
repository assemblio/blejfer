# coding=utf-8
from wtforms import Form, SelectField, RadioField

class RealEstateBasicForm(Form):

    '''
    def __init__(self, **kwargs):
        prices = range(100, 1000, 50)

        for price in range(100, 1000, 50):
            self.price_from.choices.append({
                (price, str(price))
            })

            if price > prices[0]:
                self.price_to.choices.append({
                    (price, str(price))
                })
    '''

    sale_or_rent = RadioField('Me qira / Ne shitje',
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

    cities = SelectField('City/Village',
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
            ('house','House'),
            ('office','Office'),
        ],
        default='any-type')

    price_from = SelectField('Price from', choices=[('-1', 'All')])
    price_to = SelectField('to', choices=[('-1', 'All')])

    floors = SelectField('Kateve',
        choices=[
            ('-1','Any floor'),
            ('1','1 Kateve'),
            ('1','2 Kateve'),
            ('3','1 Kateve'),
            ('4','3 Kateve'),
            ('5','4 Kateve'),
        ],
        default='-1')

    rooms = SelectField('Dhomave',
        choices=[
            ('-1','Any rooms'), # Any room
            ('1','1 Dhomave'),
            ('3','3 Dhomave'),
            ('4','4 Dhomave'),
            ('5','5 Dhomave'),
            ('6','6 Dhomave'),
            ('7','7 Dhomave'),
            ('8','8+ Dhomave'),
        ],
        default='-1')

    bathrooms = SelectField('Banjo',
        choices=[
            ('-1','Any baths'),
            ('1','1 Banjo'),
            ('2','2 Banjo'),
            ('3','3 Banjo'),
            ('4','4 Banjo'),
        ],
        default='-1')