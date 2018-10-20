[![Maintainability](https://api.codeclimate.com/v1/badges/f43594f06739f1de6901/maintainability)](https://codeclimate.com/github/Toskgreg/LuminousWayy/maintainability)
# LuminousWay
LuminousWay is a biblestudy application that provides users with the ability to ask others to join them for biblestudies and have other users request to join the biblestudies

## DESCRIPTION

LuminousWay is a platform where people can request others to join them for biblestudies.

## Link to LuminousWay on Github Pages

[LuminousWay](https://toskgreg.github.io/LuminousWay/)

## Link to LuminousWay API hosted on heroku

[LuminousWay_api](https://LuminousWay12.herokuapp.com/api/v1/biblestudies/)

### Tools

* Text editor where we write our project files. (VScode)
* Python
* Flask Python Framework -Server-side framework
* Pytest - a Python Testing Framework
* Pylint - a Python linting library 
* Postman -Application to test and consume endpoints
* PEP8 - Style guide

## Routes captured by LuminousWay

 REQUEST | ROUTE | FUNCTIONALITY
 ------- | ----- | -------------
 GET | /api/v1/biblestudies/ | Fetches all biblestudies
 POST | /api/v1/biblestudies/ | Posts a biblestudy
 GET | /api/v1/biblestudies/< biblestudyId> | Fetches a specific biblestudy
 POST | /api/v1/biblestudies/< biblestudy_id>/answer/ | Post an request to a biblestudy


## BUIT WITH

 * Flask-Python

## HOW TO RUN THE APPLICATION

 ### SETING UP THE ENVIRONMENT
 
 1. Clone this repository to your local PC

    ` git clone https://github.com/Toskgreg/ `

 2. Create a virtual environment to run application specific dependencies

    ` $ virtualenv venv `
    ` $ source venv/bin/activate `
    ` $ pip install flask `

 ### RUN THE APP

 1. To run the app

    ` python run.py `

 2. To run tests
    `  pytest tests/test.py `
## Author

**Toskin Gregory**
