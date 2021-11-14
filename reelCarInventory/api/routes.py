from flask import Blueprint, request, jsonify

from reelCarInventory.helpers import token_required
from reelCarInventory.models import db,User,Car,car_schema,cars_schema

api = Blueprint('api',__name__,url_prefix='/api')

@api.route('/getdata')
@token_required
def getdata(current_user_token):
    return { 'some': "value" , 
            'other': 'Data' }

# CREATE CAR ENDPOINT
@api.route('/cars', methods = ['POST'])
@token_required
def create_car(current_user_token):
    name = request.json['name']
    description = request.json['description']
    price = request.json['price']
    transmission = request.json['transmission']
    drivetrain = request.json['drivetrain']
    max_speed = request.json['max_speed']
    cost_of_prod = request.json['cost_of_prod']
    series = request.json['series']
    user_token = current_user_token.token
     # dimensions = request.json['dimensions']
    # weight = request.json['weight']
     # cam_quality = request.json['cam_quality']
    # flight_time = request.json['flight_time']

    print(f'BIG TESTER: {current_user_token.token}')

    car = Car(name,description,price,transmission,drivetrain,max_speed,cost_of_prod,series,user_token =current_user_token.token )
    db.session.add(car)
    db.session.commit()

    response = car_schema.dump(car)
    return jsonify(response)


# RETRIEVE ALL CARs ENDPOINT
@api.route('/cars', methods = ['GET'])
@token_required
def get_cars(current_user_token):
    owner = current_user_token.token
    cars = Car.query.filter_by(user_token = owner).all()
    response = cars_schema.dump(cars)
    return jsonify(response)  
    

# RETRIEVE ONE CAR ENDPOINT
@api.route('/cars/<id>', methods = ['GET'])
@token_required
def get_car(current_user_token, id):
    owner = current_user_token.token
    if owner == current_user_token.token:
        car = Car.query.get(id)
        response = car_schema.dump(car)
        return jsonify(response)
    else:
        return jsonify({"message": "Valid Token Required"}),401


# UPDATE CAR ENDPOINT
@api.route('/cars/<id>', methods = ['POST','PUT'])
@token_required
def update_car(current_user_token,id):
    car = Car.query.get(id) # GET DRONE INSTANCE

    car.name = request.json['name']
    car.description = request.json['description']
    car.price = request.json['price']
    car.transmission = request.json['transmission']
    car.drivetrain = request.json['drivetrain']
    car.max_speed = request.json['max_speed']
    car.cost_of_prod = request.json['cost_of_prod']
    car.series = request.json['series']
    car.user_token = current_user_token.token

    db.session.commit()
    response = car_schema.dump(car)
    return jsonify(response)


# DELETE CAR ENDPOINT
@api.route('/cars/<id>', methods = ['DELETE'])
@token_required
def delete_car(current_user_token, id):
    car = Car.query.get(id)
    db.session.delete(car)
    db.session.commit()
    
    response = car_schema.dump(car)
    return jsonify(response)