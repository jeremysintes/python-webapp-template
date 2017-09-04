voir http://pyscaffold.readthedocs.io/en/v2.5.7/
voir http://yeoman.io/
https://jeffknupp.com/blog/2013/08/16/open-sourcing-a-python-project-the-right-way/
https://cookiecutter.readthedocs.io/en/latest/usage.html


# CHECKLIST

## PRE-REQUISITES
- nodejs : https://nodejs.org/en/ (?)
- anaconda for the environment creation (ou virtualenv)


## PRODUCTION
Remove debug mode



## GIT

- Clone the template
	`git clone https://github.com/jeremysintes/python-webapp-template/`


- Use git flow cheatsheet
	http://danielkummer.github.io/git-flow-cheatsheet/index.fr_FR.html




## DEVELOPMENT ENVIRONMENT

- Create an environment (with conda for exemple)
	`conda env create -n NAME_OF_THE_PROJECT`

- Activate the environment 
	`activate NAME_OF_THE_PROJECT`

From the root
- Install the minimum requirements to run the app
	(NAME_OF_THE_PROJECT) $ `pip install -r requirements.txt`



## NAME

- Replace NAME_OF_THE_PROJECT by the name of your app
	With Sublime Texte : use `find` > `find in files`
	http://docs.sublimetext.info/en/latest/search_and_replace/search_and_replace_files.html
	Do not forget to rename the main folder as well


## RUNNING


To run the application in the development web server just execute `run.py` with the Python interpreter from the flask virtual environment :

- Activate the environment 
	`$ activate NAME_OF_THE_PROJECT`

- Start the app
	from the root
	(NAME_OF_THE_PROJECT) $ `python run.py`


- If everything is working properly commit
	`git commit -m "initial commit"`




## LICENSE

- Choose a license (https://choosealicense.com)

- navigate to the main page of the repository GUI

- click __Create new file__

- In the file name field, type LICENSE (with all caps)

- click __Choose a license template__

- select a license from the list

- review and submit

- commit



## FRONT END

### LAYOUT

- complet description
- complet keyword
- replace favicons
- replace icon in nav bar


### DESIGN

Bootstrap is the HTML, CSS, and JS framework selected by default in the template file.

To consult the components available : 
	https://getbootstrap.com/docs/3.3/components/



## TESTS

voir py.test
voir tox
voir jasmine de materialize
voir https://travis-ci.org/




## OPEN SOURCE PROJECT

### CODE OF CONDUCT

- install the Contributor Covenant node module ?
	`npm install -g covgen`

- Generate the Contributor Covenant
	`covgen <your mail address>`	

- Look for more information on how to use the Contributor Covenant and how to enforce it
	https://contributor-covenant.org/




## SHARING

### REQUIREMENTS
from the root
- Generate your requirements.txt file automatically 
	`pip install pipreqs`
	`pipreqs --force .`

- Commit
	`git commit -m "adding requirements.txt"`


### SETUP

Voir Setutptools

### MANIFEST.in

- Check the completness of you manifest (https://pypi.python.org/pypi/check-manifest)
from the root
`pip install check-manifest`
`check-manifest`


### PyPI 

	--> See setuptools documentation for more info concerning binary distribution

- Sanity check first with cheesecake

- first time? Register your package (account on PyPI required)
	`python setup.py register`
 
- create your distributable package and upload it to PyPI
	`python setup.py sdist upload`



## DOCUMENTATION

Tuto : http://thomas-cokelaer.info/tutorials/sphinx/quickstart.html
http://docs.python-guide.org/en/latest/writing/documentation/
https://realpython.com/blog/python/generating-code-documentation-with-pycco/

- Install Sphynx in your environment
	`pip install sphynx`

- Autogenerate your doc
	`sphinx-apidoc -F -o docs NAME_OF_THE_PROJECT`


voir https://realpython.com/blog/python/generating-code-documentation-with-pycco/

voir https://docs.readthedocs.io/en/latest/webhooks.html


## PROJECT MANAGEMENT
### CHAT
https://gitter.im/ or Slack?

### TASK MANAGER
Trello


### PRIVACY by DESIGN
Génération automatique des textes réglementaires (DPIA, Confidentiality Policy, ...)


### SECURE by DESIGN
Dev Sec Ops? Intégrer éléments de pen test dans l'intégration continue?

### API First design 
https://github.com/jeffknupp/sandman2
https://swagger.io/
https://flask-restful.readthedocs.io/en/0.3.5/	
https://www.fullstackpython.com/api-creation.html
https://medium.com/adobe-io/three-principles-of-api-first-design-fa6666d9f694
or SAAS?
http://www.api-first.com/
https://apievangelist.com/2014/08/11/what-is-an-api-first-strategy-adding-some-dimensions-to-this-new-question/
https://dzone.com/articles/an-api-first-development-approach-1

## SOURCES
https://jeffknupp.com/blog/2014/02/04/starting-a-python-project-the-right-way/
https://jeffknupp.com/blog/2013/08/16/open-sourcing-a-python-project-the-right-way/
http://docs.python-guide.org/en/latest/writing/structure/