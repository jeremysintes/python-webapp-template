from flask import Flask, request


app = Flask(__name__)


from NAME_OF_THE_APP import views


__VERSION__ = 0.0

# [N!]N(.N)*[{a|b|rc}N][.postN][.devN]
# For more information : https://www.python.org/dev/peps/pep-0440/