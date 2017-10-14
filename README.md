# pwx-app
pwx-app is a simple API allowing users to view, create, update and delete Categories and Products to generic marketplace.


### Requirements

- Python 3
- SQLite
- Flask
- Flask-SQLAlchemy
- Flask-Admin
- Flask-Migrate
- Flask-Restless

### Instructions to local deploy
```shell
$ git clone https://github.com/romuluc/pwx-app.git

$ cd pwd-app

$ pip install -r requirements.txt

$ export FLASK_CONFIG=development

$ export FLASK_APP=run.py

$ flask run
```

### Usage (with curl tool)
 
 - Get categories
 ```shell
 $ curl http://localhost:5000/api/category
 ```
 
 - Get specif category
 ```shell
 $ curl http://localhost:5000/api/category/2
 ```
 
 - Post category
 ```shell
 $ curl http://localhost:5000/api/category -H "Content-Type: application/json" -X POST -d '{"name":"Sanduíchess"}' -v
 ```
 
 - Update category
 ```shell
$ curl http://localhost:5000/api/category/5 -H "Content-Type: application/json" -X PUT -d '{"name":"Diversoss"}'
 ```
 
 - Delete category
 ```shell
 $ curl http://localhost:5000/api/category/5 -X DELETE -v
 ```
 
  - Post product
 ```shell
 $ curl http://localhost:5000/api/product -H "Content-Type: application/json" -X POST -d '{"name":"Refrigerente 2L", "price": 10.0, "category_id": 3}' -v
 ```
 
 - Search (Example: Searching products wich price greater than 10)
 ```shell
 $ curl \
  -G \
  -H "Content-type: application/json" \
  -d "q={\"filters\":[{\"name\":\"price\",\"op\":\"ge\",\"val\":10}]}" \
  http://127.0.0.1:5000/api/product
  ```
  
  - Admin
  http://localhost:5000/admin
 
 
 
 
 
 


