import re
from flask import Flask, render_template, request, jsonify, make_response

app = Flask(__name__) #creamos un objeto y inicializamos flask

@app.route('/') 
def home(): 
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/', methods=['POST', 'GET'])
def validar():
    password = request.form['contrasena']
    obtener = re.compile("^[A-Z][0-9]{3}[a-z]+[\W]{3}$")
    validador = obtener.match(password)
    if(validador is not None):
        return make_response(jsonify("La contraseña es segura"),200)
    else:
        return make_response(jsonify("La contraseña es insegura"),404)


if __name__ == '__main__':
    app.run(debug = True)# iniciamos un servidor
