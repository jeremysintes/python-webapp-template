# CONTRIBUTING

## ADD HTML PAGE

- Create a new HTML page in NAME_OF_THE_APP/templates 

- Start your file with :
	`{% extends "base.html" %}
	{% block content %}`

- End your file with :
	`{% endblock %}`

- In /NAME_OF_THE_APP/views.py, add 

		@app.route('/NAME_OF_YOUR_HTML_FILE')
		def NAME_OF_YOUR_HTML_FILE():
			return render_template("NAME_OF_YOUR_HTML_FILE.html", title='TITLE_OF_YOUR_HTML_FILE')


### jinja tips 

- add variables in views.py as VAR1 to be used in your HTML page with `{{VAR1}}`
	
		@app.route('/NAME_OF_YOUR_HTML_FILE')
		def NAME_OF_YOUR_HTML_FILE():
			return render_template("NAME_OF_YOUR_HTML_FILE.html", title='TITLE_OF_YOUR_HTML_FILE', VAR1= VAR1, VAR2= "exemple of string var")



	


- add FOR or IF logic in your HTML file
		`{% for ... in ... % }
		[your code]
		{ % endfor % }`


### static file tips

- put your files in NAME_OF_THE_APP/static

- use the path `{{ url_for('static',filename='PATH/FROM/STATIC/FOLDER')}}`