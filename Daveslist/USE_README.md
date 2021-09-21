# Daveslist
------------

# Installing
------------

# Docker-Compose

```
$ docker-compose up -d
$ docker-compose exec web bash
$ cd Daveslist
$ pip3 install -r requirements.txt
$ python3 manage.py runserver 0.0.0.0:8000


```

This command will sintall the docker env for our service
and will be run on 0.0.0.0:8000


## Structure
In a RESTful API, endpoints (URLs) define the structure of the API and how end users access data from our application using the HTTP methods - GET, POST, PUT, DELETE. Endpoints should be logically organized around _collections_ and _elements_, both of which are resources.

In our case, we have one single resource, `books`, so we will use the following URLS in api `/api/`:

Endpoint |HTTP Method | CRUD Method | Result
-- | -- |-- |--
`welcome`   | GET | READ | Get all endpoints
`books`     | GET | READ | Get all books
`register`  | POST | CREATE | Create a new user

`my_books` | GET | READ | Get all user books
`upload`   | POST | CREATE | Upload a new book reference
`update/<int:book_id>` | PUT | Update | Update a book reference
`delete/<int:book_id>` | DELETE | DELETE | Delete a book reference


## Use

There are the docs based in openApi and swagger, where you can test the endpoints

There an issue and you cant not seet update and delete endpoints in documentation.
- openAPi: http://127.0.0.1:8000/openapi/
- swagger: http://127.0.0.1:8000/docs/


With Httpie also you can try the endpoints

[httpie](https://github.com/jakubroztocil/httpie#installation)


Httpie is a user-friendly http client  Let's try that.

## Public endpoints

- Register a user
http post http://127.0.0.1:8000/api/register username=evertcolombia author=elvago5 password=changethis

- get all uploaded books
http get http://127.0.0.1:8000/api/books

## Private endpoints

For this endpoints you will need generate a JWT

- get Token
http post http://127.0.0.1:8000/api/token/ username=evertcolombia password=changethis

- get user upladed books
http get http://127.0.0.1:8000/api/my_books 'Authorization:Bearer eyJ0.....' \

- create a new book register 
http get http://127.0.0.1:8000/api/upload 'Authorization:Bearer eyJ0.....' \
    book:='{"title": "1984", "description": "The end of the normality", "price": 20.00}''

- update a book register (need pass register ID)
http put http://127.0.0.1:8000/api/update/3 'Authorization:Bearer eyJ0.....' \
    book:='{"title": "cien anios de soledad", "description": "una fantasia en macondo", "price": 20.00}'

- delete  a book register (need pass register ID)
http put http://127.0.0.1:8000/api/delete/3 'Authorization:Bearer eyJ0.....' \


# There is a user created for you user whit the follow credentials

{
    "author": "Dark",
    "password": "changethis",
    "username": "_Darth_Vader_"
}