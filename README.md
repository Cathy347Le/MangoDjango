# MangoDjango
Django Hackathon Project

Pet E-Commerce site built with Python, Django and Bootstrap.

<img width="1280" alt="Screen Shot 2019-04-05 at 4 23 47 PM" src="https://user-images.githubusercontent.com/46323883/55655195-8436cf80-57c1-11e9-80f0-ddeb518af8ef.png">


### Getting Started

Clone the repo.
cd into the folder:

```
cd MangoDjango  
```

### Prerequisites

To run this repo please have Python 3 and pip installed.  PostgresSQL also needs to be installed and running.

### Installing

Installation


Run the following command to install dependencies:

```
pipenv install
```

Then run the following command to enter the virtual environment:

```
pipenv shell
```
Set up your PostqreSQL database and make your migrations to run the seed file

```
psql -U postgre -f settings.sql
python3 manage.py makemigrations
python3 manage.py migrate


```
Lastly, run this command to run the server:

```
python3 manage.py runserver
```

To access the front-end navigate to http://localhost:8000 in your browser.
To access the back-end navigate to http://localhost:8000/admin in your browser.


### Deployment

The app is currently not deployed live and must be run locally

###


### Authors

Team MangoDjango
[Konjo] (https://github.com/konjoinfinity)
[Cathy Le] (https://github.com/Cathy347Le)
[Jasmin Vargas](https://github.com/jasvr
[Yoshi Maisami](https://github.com/yoshimaisami)


### Acknowledgments
Big thanks to…
- Casey Jennings for her “Wags to Wings” vision, mockups and visual design assets
- Zakk Fleischmann & Hammad Malik for their instruction & encouragement  
- Lemuel Boyce for his Drift.com [Django Hack] (https://github.com/rhymiz)
- Christian Hess for his [Shuup djnago e-commerce tutorial[ (https://medium.com/@chessbr/creating-your-first-e-commerce-with-shuup-open-source-platform-part-1-72bb3bd32b23)
- Daniel Roseman - (Django users) https://groups.google.com/forum/#!topic/django-users/pIdxv0PJwBY
