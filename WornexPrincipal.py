from flask import Flask, render_template, request

app = Flask(__name__)

USUARIO = "WorNex"
CONTRASENA = "WN2026"

# Pantalla principal
@app.route('/')
def inicio():
    return render_template('InterfazPrincipal.html')

# Subpantalla de credenciales
@app.route('/login')
def login():
    return render_template('InterfazCredenciales.html')

# Validación de credenciales
@app.route('/validar', methods=['POST'])
def validar():

    usuario = request.form['usuario']
    contrasena = request.form['contrasena']

    if usuario == USUARIO and contrasena == CONTRASENA:
        return render_template('InterfazTecnico.html')
    else:
        return '''
        <h2>Usuario o contraseña incorrectos</h2>
        <a href="/">Volver</a>
        '''

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)