# poc-flask
POC Rest API using Flask that allows you to create, update and retrieve Person objects stored in a MongoDB NoSQL database.

## Configuration
Default MongoDB config in flask\_rest_service/\__init__.py file:

```
MONGO_URL = "mongodb://localhost:27017/poc";
```

## How to run
Install packages/dependencies: 
```
pip install -r requirements.txt
```

Running "runserver.py" file you should be able to visit the rest service at http://localhost:5000 and get an "OK" status.
```
python runserver.py 
```

## Rest API examples
GET
```
curl http://localhost:5000/persons
curl http://localhost:5000/persons/{ID}
```

POST
```
curl -i -X POST -H "Content-Type:application/json" -d '{  "firstName" : "Marty",  "lastName" : "McFly" }' http://localhost:5000/persons
```

PUT
```
curl -X PUT -H "Content-Type:application/json" -d '{ "firstName": "Emmett", "lastName": "Brown" }' http://localhost:5000/persons/{ID}
```

DELETE
```
curl -X DELETE http://localhost:5000/persons/{ID}
```
