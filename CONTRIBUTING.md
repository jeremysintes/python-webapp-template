# CONTRIBUTING

## FIRST STEP

1. To create a new HTML page :

- Create a new HTML page in NAME_OF_THE_APP\templates
- Start your file with :
	`{% extends "base.html" %}
	{% block content %}`
- End your file with :
	`{% endblock %}`



- In \NAME_OF_THE_APP\views.py, add :
	`@app.route('/index')
	def index():
    return render_template("index.html",
                           title='Home',URL_ES= URL_ES, AUTH_ES = AUTH_ES)
where you replace index by the name of your page, and do not forget to indicate your HTML page in render_template too and @app.route
Furthermore you can add variables to your html page (like URL_ES and AUTH_ES), and call them by using Jinja syntax in the HTML CODE of your page
If you want to call a variable use the following syntax:
For instance {{URL_ES}}
You can also use For or IF instruction by using:
{% for ... in ... % }
[your code]
{ % endfor % }
Forms can be a variable, very useful to keep and use what someone have chosen in your website in order to execute something in python in your code. 

2°) If you want to use some static file, you will have to put it inside of app\static and to refers it by using the following 
For instance: {{ url_for('static',filename='Materialized/js/plugins/google-map/google-map-script.js')}} Give the path since the static folder

3°) You can use dynamic content by using Javascript in your HTML code, cool in order to use API, requests in an ElasticSearch Database (in AJAX *), or Kibana Dashboard.

*: An easy way to learn how to make requests in AJAX with ElasticSearch Database is to use Postman (Google Apps on Chrome), and click on the code button in the top right corner.

4°) Inside the created python function in 1°), you can implement Python Code in order to give variables as outputs in render_template. If you want to use your own python function, you will have to put in the root folder. 

5°) Tips 
- Do not forget to catch errors in views.py by using try/except instance