#Importando o módulo flask no projeto
from flask import Flask

#Crie um objeto da classe Flask
app = Flask(__name__)

#A função route() da classe  Flask
@app.route("/")

# A URL ‘/’ é ligada à função first_flask.
def first_flask():

    return "Este é meu primeiro programa Flask"

# Execute a aplicação no servidor local
app.run()
