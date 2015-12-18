# coding=utf-8
from wtforms import IntegerField, DecimalField, StringField, TextAreaField, SelectMultipleField
from app.common.realestate_basicform import RealEstateBasicForm

class RealEstateEntryForm(RealEstateBasicForm):

    price = IntegerField('Çmimi')
    address = StringField('Adresa')
    description = TextAreaField('Pershkrimi')
    amenities = SelectMultipleField('Stabilimentet',
        choices=[
            ('Enë larësi','Enë larësi'), # Dishwasher
            ('Larësi / Tharësi','Larësi / Tharësi'), # Washer / Dryer
            ('Nxemje Qendrore','Nxemje Qendrore'), # Central Heating
            ('Tjera','Tjera') # Other
        ])

    size = IntegerField('Madhësia')
    seller = StringField('Adresa')
    phone = StringField('Telefoni')
    viber = StringField('Viber')
    email = StringField('E-mail')

    latitude = DecimalField('Latitude')
    longitude = DecimalField('Longitude')

