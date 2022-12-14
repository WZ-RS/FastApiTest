# FastAPI and MongoDB Boilerplate

POC App for WZ RestAPI

## Features

+ Python FastAPI backend.
+ MongoDB database.
+ Authentication
+ Deployment

## Local Docker Setup

To run the application locally using Docker, follow these steps:

1. Clone this repository

2. Build the Docker images

```console
docker-compose build
```

3. Start the Docker images

```console
docker-compose up -d
```

## Dev Setup

To use the application, follow the outlined steps:

1. Clone this repository and create a virtual environment in it:

```console
$ python -m virtualenv .
```

2. Install the modules listed in the `requirements.txt` file:

```console
(venv)$ pip3 install -r requirements.txt
```
3. You also need to start your mongodb instance either locally or on Docker as well as create a `.env.dev` file. See the `.env.sample` for configurations.

4. Start the application:

```console
python main.py
```


The starter listens on port 8000 on address [0.0.0.0](0.0.0.0:8080). 

![FastAPI-MongoDB starter](https://user-images.githubusercontent.com/31009679/165318867-4a0504d5-1fd0-4adc-8df9-db2ff3c0c3b9.png)

## Deployment

This application can be deployed on any PaaS such as [Heroku](https://heroku.com).

## License

This project is licensed under the terms of MIT license.
