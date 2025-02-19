# Astrophysics Dashboard
![Python](https://img.shields.io/badge/python-%23F0F0F0?style=for-the-badge&logo=data%3Aimage%2Fpng%3Bbase64%2CiVBORw0KGgoAAAANSUhEUgAAADAAAAAwCAYAAABXAvmHAAAACXBIWXMAAAsTAAALEwEAmpwYAAADGUlEQVR4nO2YPWgUQRTHZ2dzM5dYaCFBAiaFNkZRBMUuiI0fRdBCwSZFolj4kWCSmRMJhyksBJVgI2qhhYIpFEREczPZmUSDSBo%2FkIAERWMnETQmSDRPdm89g4TczCXrXnD%2F8Jpr9vfb92Z25hBKkiRJEoTAQTy3GWcEd7i8i7l4hZkYx0x%2Bx1xMYi4%2BYCaeOlxecrncgbJZXD5vrUNsDIC5BNNyuHiITnor40ZHKHuvCjM5ZgNfKCaHYu%2BEy%2Fp3lgQflpvJ7YpVAHPZHL7NMXRK1COeq8VcvrAYpe54BZhoy4PIa39%2Bk13mAvJiWQgUOtAu6%2Bw6IMtEoMRyEoGYu%2BSEHQBN2kBTmFVToOkzUGTfUhWAoBSdAU0Plf70jLfW4fJy%2BKWdWMi8lySgg%2FoKMl1nze52ykbM5LfFhi5BAEDRs3b0%2Be1w0d%2F4HALnzQTIqBW%2Fw0VP1PBBMXEsEFDk9LwCfnlVq4wFMBNvohcQn1H7o%2Bp8B%2BjtogKK7DGjb%2FVWYC5mIhaY8A%2BCyId%2Fsqw6WKjFBVrNBHhuezTjIn9iJt87TF5FHXLN78eBpreKwufrjNn4ZORBy1EYwVw2oc6%2BmuBmZhgAhEHRC4bw%2Fk50zkyAi6Pmu4i4iY4%2FoKbQhZFRqQOg6LAxfH6EuJkAEy2GW2A%2FynoVAdTjyhrQtAc0eQua%2FrAC06YC6SYjAbdT7DWZZ8T61gXwXsUW0ORTJNB6Vg2mNpn1mMn1BgJDeXiUBk3eRQ6v6CQMo5SZwP5et9hX2OHiSiCgSGPk8DqoO8gmDhPS6AyjyIl%2FAD%2Ftj6mVAGbiiJFAsTPMYsAr2oysw3PL5%2Fu%2FJ2KBKdD0NShy3XzhzhGXid2YiemSBRSN98IehMsGf7%2F%2F%2B16wdASKZMEjpGKW%2FM8EyBgMkHrQ6dWg6POlJ6BI4e9H0KSrTARoi4XAR%2FBSG2AwXQuavgwFuuMVCEZiAWvAo4djFTC%2Bz869gL9YXdQjExhGVaDJDTt4Mgo63YDKKaAqtvrXPlBEh0fsifAsMw6KjoCi90GRLAxUboNe5MbNmyRJElQe%2BQWgfIcmva%2Bj%2BwAAAABJRU5ErkJggg%3D%3D)
![Flask](https://img.shields.io/badge/flask-%232BAED5?style=for-the-badge&logo=flask)
![Plotly Dash](https://img.shields.io/badge/plotly_dash-%233F4F75?style=for-the-badge&logo=plotly)
![Pandas](https://img.shields.io/badge/pandas-%23150458?style=for-the-badge&logo=pandas)
![Bootstrap5](https://img.shields.io/badge/bootstrap-%237952B3?style=for-the-badge&logo=bootstrap&logoColor=white)


## Table of Contents
 - [About](#about)
 - [Project Setup](#project-setup)
 - [Dependencies](#dependencies)
 - [Execution](#execution)

## About
 A dashboard style interactive web application for visualizing astrophysics data, to aid in exoplanets discovery.
 
 This application is similar to one I made for the Institute of Astrophysics and Space Sciences / Astrophysics Centre of the University of Porto. Comparing to the original one, this application has some details modified to not use their intellectual property. The original one accesses their API for data, whilst this one uses a different data source.

 <img width="500" alt="screenshot" src="https://github.com/carlahnr/astrophysics_dashboard/assets/100738389/47cd75de-242d-4be5-a757-371efa21eff8">

## Project Setup

### General GUI setup
 The app contains 3 views:
 - **Home view:** description of the app.
 - **Dashboard view:** main funcionality view, with all data visualization resources.
 - **Sourcepath management view:** view to add and remove sourcepaths to the Dashboard.

### Directories structure
 - **/ :** root directory of the project, with the Python application. Also contains the project's metadata files, and configuration files.
 - **/static :** all static assets, such as images, icons, Javascript and CSS files.
 - **/templates :** templates for the views using mainly HTML and Jinja.

### Techstack
 Made in Python, it uses Plotly Dash for the data visualization elements and UI, Pandas for data manipulation, Flask microframework as the web server gateway interface (WSGI). It uses Jinja, HTML, JavaScript, and is styled with CSS (Bootstrap 5 and Dash Bootstrap). For more details, see [Dependencies](#dependencies).
 
 - Python (3.9.18)
 - Flask
 - Plotly Dash
 - Pandas
 - Bootstrap

## Dependencies

### Getting Started with Plotly Dash
[Plotly Dash](https://dash.plotly.com/installation) framework is used for data visualization UI items. Using Plotly (5.22.0) and Dash (2.17.1).

### Getting Started with Flask
Web framework used was [Flask](https://flask.palletsprojects.com/en/3.0.x/installation/#install-flask) (3.0.2). Application uses [Jinja](https://jinja.palletsprojects.com/en/3.1.x/intro/#installation) (3.1.3) templating.

### Getting Started with Pandas
Data manipulation uses [Pandas](https://pandas.pydata.org/getting_started.html)  (2.2.2).

### Getting Started with Bootstrap
Styled with [Bootstrap 5](https://getbootstrap.com/docs/5.2/getting-started/download/). Also uses [Dash Bootstrap Components](https://dash-bootstrap-components.opensource.faculty.ai/docs/) (1.6.0) and [Dash Bootstrap Templates](https://pypi.org/project/dash-bootstrap-templates/) (1.1.2).

## Execution
- `export FLASK_APP=app.py`
- `flask run --port 5001`, to run on a different port, change the port number.
