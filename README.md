# TRIVIAL APP: HandsOn

## About

<img align="left" width="100" height="100" src="https://user-images.githubusercontent.com/61190134/76793662-b6b8bd00-67c5-11ea-83b2-efcc9ed462fc.png">

*Instructor*: [Jordi Mateo Fornés](http:jordimateofornes.com)

*Course*: [Grau en Tècniques d'Interacció Digital i de Computació](http://www.grauinteraccioicomputacio.udl.cat/ca/index.html)

*University*: University of Lleida - Campus Igualada - Escola Politècnica Superior

## Purpose

![trivial](https://user-images.githubusercontent.com/61190134/160235652-58210d7e-90f5-4487-8e3d-6c1d3191b30e.png)

* We use Databindings and MVVM
* We use Retrofit to exchange information between a Client (Android App) and a Backend with a database.


## Description

Simple backend and database that provides a set of multiple-choice (questions and answers). This is a starter kit to code the Trivial App using JAVA and Android during the class.

@GET http://127.0.0.1:8000/trivial/question

```json
{
    "id": 9,
    "question": "The minimum number of frames to be allocated to a process is decided by the ____________",
    "category": "os",
    "answers": [
        {
            "id": 33,
            "answer": "the amount of available physical memory",
            "is_correct": false
        },
        {
            "id": 34,
            "answer": "operating System",
            "is_correct": false
        },
        {
            "id": 35,
            "answer": "instruction set architecture",
            "is_correct": true
        },
        {
            "id": 36,
            "answer": "none of the mentioned",
            "is_correct": false
        }
    ]
}
```

```sh
curl --location --request GET '127.0.0.1:8000/trivial/question'
```

## How to use it

* Clean the container to avoid conflicts with your own project.
  
```sh
docker system prune -a
```

* Go to docker folder inside backend

```sh
docker-compose up --build 
```
# TrivialApp-HandsOn-MVVM
