# Setting up React and Django as separate servers
---
**Code:** All code can be found in the map: `3_Seperate_Servers`.

### Project Setup

- Create a new project directory. 
- [Create your React frontend](Create%20a%20React%20Project.md)
- [Create your Django project](Setting%20up%20Django.md) in the same folder.

### Running the servers
- Run `npm start` in the react folder.
	- This will open your project in a web browser, usually at http://localhost:3000
- Run `python manage.py runserver`
	- You typically can access the server at http://localhost:8000

To let these two communicate you have to use Django's RESTful API in React.