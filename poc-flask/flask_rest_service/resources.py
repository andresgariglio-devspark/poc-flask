import json
from flask import request, abort
from flask.ext import restful
from flask.ext.restful import reqparse
from flask_rest_service import app, api, mongo
from bson.objectid import ObjectId


parser = reqparse.RequestParser()
parser.add_argument('firstName', type=str, help='The first name')
parser.add_argument('lastName', type=str, help='The last name')

class Persons(restful.Resource):
    def get(self):
        return  [x for x in mongo.db.person.find()]

    def post(self):
        args = parser.parse_args()
        print args
        person_id =  mongo.db.person.insert(args)
        return mongo.db.person.find_one({"_id": person_id})


class Person(restful.Resource):
    def get(self, person_id):
        return mongo.db.person.find_one_or_404({"_id": person_id})

    def delete(self, person_id):
        mongo.db.person.find_one_or_404({"_id": person_id})
        mongo.db.person.remove({"_id": person_id})
        return '', 204




class Root(restful.Resource):
    def get(self):
        return {
            'status': 'OK',
            'mongo': str(mongo.db),
        }

api.add_resource(Root, '/')
api.add_resource(Persons, '/persons')
api.add_resource(Person, '/persons/<ObjectId:person_id>')
