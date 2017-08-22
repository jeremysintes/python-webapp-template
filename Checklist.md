voir http://pyscaffold.readthedocs.io/en/v2.5.7/
voir http://yeoman.io/
https://jeffknupp.com/blog/2013/08/16/open-sourcing-a-python-project-the-right-way/
https://cookiecutter.readthedocs.io/en/latest/usage.html


# CHECKLIST

## PRE-REQUISITES
- nodejs : https://nodejs.org/en/
- anaconda for the environment creation (ou virtualenv)




## GIT

- Clone the template
	`git clone https://github.com/jeremysintes/python-webapp-template/`

- Git flow cheatsheet
	http://danielkummer.github.io/git-flow-cheatsheet/index.fr_FR.html




## DEVELOPMENT ENVIRONMENT

- Create an environment (with conda for exemple)
	`conda env create -n NAME_OF_THE_APP`

From the root
- Install the minimum requirements to run the app
	`pip install -r requirements.txt`



## NAME

- Replace NAME_OF_THE_APP by the name of your app
	- Folder at the root
	- README
	- run.py
	- .travis.yaml
	- .gitignore
	- NAME_OF_THE_APP > views.py
	- NAME_OF_THE_APP > __init__.py
	- NAME_OF_THE_APP > tests > tests_NAME_OF_THE_APP.py



## RUNNING


To run the application in the development web server just execute `run.py` with the Python interpreter from the flask virtual environment :

- Activate the environment 
	`$ activate NAME_OF_THE_APP`

- Start the app
	from the root
	`(NAME_OF_THE_APP) $ python run.py`


- If everything is working properly commit
	`git commit -m "initial commit"`




## LICENSE

- Choose a license (https://choosealicense.com)

- Update the LICENSE file

- commit
	`git commit -m "Choosing the appropriate license"`




## LAYOUT

- complet description
- complet keyword
- replace favicons
- replace icon in nav bar



## DESIGN

Bootstrap is the HTML, CSS, and JS framework selected by default in the template file.

To consult the components available : 
	https://getbootstrap.com/docs/3.3/components/




## TESTS

voir py.test
voir tox
voir jasmine de materialize





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

https://realpython.com/blog/python/generating-code-documentation-with-pycco/

- Install Sphynx in your environment
	`pip install sphynx`

- Autogenerate your doc
	`sphinx-apidoc -F -o docs NAME_OF_THE_APP`




## PROJECT MANAGEMENT
	### CHAT
	https://gitter.im/ or Slack?

	### TASK MANAGER
	Trello

	
	### PRIVACY by DESIGN
	Génération automatique des textes réglementaires (DPIA, Confidentiality Policy, ...)


	### SECURITE by DESIGN
	Dev Sec Ops? Intégrer éléments de pain test dans l'intégration continue?
