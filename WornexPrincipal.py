from flask import Flask, render_template

app = Flask(__name__)
app.secret_key = 'Inicio_sesion_WorNex'

# Credenciales


@app.route('/')
def inicio():
    return render_template('InterfazPrincipal.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)