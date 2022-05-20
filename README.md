# Check-Point Home Assignment - Django REST API 

## Depedencies 
 - Python 3.9 
 - Django 4.0.4
 
## Usage
### To turn on the server:
  - Goto main package -> check_point_dj
  - run: 'python manage.py runserver'

### To access the API via curl:
- http://localhost:8000/api/v1/events 
- http://localhost:8000/api/v1/stats?interval=<integer>
  
### Access Admin Page:
- You can access the admin page at http://localhost:8000/admin/
- username: admin,  password: 0


## Testing
- run 'python manage.py test' to run all tests

## File Structure
### 'key_words_api' package holds modules responsible for making Django run.
- Most importantly this includes ulrs.py and settings.py that map our URLs and control settings respectively. 

### 'events_app' is our Django app for our events API v1.
1. urls.py:
    - maps the internal URLs of the api.
2. models.py:
   - This holds our Model "EventItem" that represents a row in an SQLite Database.
3. views.py:
   -  In Django views are functions/classes that take requests & return responses.
   - We define here 2 views, one for each of our api endpoints.

##### Note: Django is structured as MVT(Model View Template).
##### Unlike MVC the View in Django is more of a Service Layer.

## DB Structure  
#### This API has only one table - to hold EventItems
#### Each EventItem has:
- data - in the forma of a string.
- stats - Json object, counter of key-word occurences.
- a timestamp - datetime.datetime object.

  
## Assumptions
1. Was not clear exactly what interval was - I assumed that it meant get interval seconds back
2. I assumed we tally only full words.
3. I assumed the search is case insensitive.
  
  
