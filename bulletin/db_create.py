import requests

from django.core.files import File

from bulletin_board.models import Car, Photos

#TODO

def db_create(car_title='', price='', seller='', phone='', car_description='', avito_item='', car_brand='', car_model='', car_generation='', 
modification='', year_of_manufacture='', car_mileage='', condition='', owners='',vin_number='', type_chassis='', doors='', engine_type='', transmission='', drive='',
steering_side='', color='', equipment='', view_place='', engine_volume='', images ='' ):

    sale_announcement = Car(car_title=car_title, price=price, seller=seller,phone=phone, car_description=car_description, avito_item=avito_item, 
    car_brand=car_brand, car_model=car_model, car_generation=car_generation, modif=modification, year_of_manufacture=year_of_manufacture, car_mileage=car_mileage, condition=condition,
    owners=owners, vin_number=vin_number, type_chassis=type_chassis, doors=doors, engine_type=engine_type, transmission=transmission, drive=drive, steering_side=steering_side, 
    color=color, equipment=equipment, view_place=view_place, engine_volume=engine_volume)

    sale_announcement.save()

    for image in images:
        url = image
        photo = Photos(image_url = url, car = sale_announcement)
        photo.save()
        photo.get_remote_url()

    return print('Объявление занесено в базу данных')
