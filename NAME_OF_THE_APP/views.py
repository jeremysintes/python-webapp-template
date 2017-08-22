from NAME_OF_THE_APP import app
from flask import render_template

#--------------------------------------------------------------------------------------------------------------------
#   ACCUEIL:
#   Tous les templates liés à l'accueil de l'utilisateur
#
#--------------------------------------------------------------------------------------------------------------------

# Page d'accueil
@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html",
                           title='Home')