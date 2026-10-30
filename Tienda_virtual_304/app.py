from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)
# Pantalla de bienvenida
@app.route('/')
def bienvenida():
    return render_template('pantalla_de_vienvenida.html')
# Pantalla de inicio de sesión
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = request.form.get('usuario')
        contrasena = request.form.get('contrasena')
        # Aquí puedes agregar la validación de usuarios
        if usuario and contrasena:
            return redirect(url_for('catalogo'))
        return render_template('index.html', error='Completa todos los campos')
    return render_template('index.html')
# Catálogo
@app.route('/catalogo')
def catalogo():
    return render_template('catalogo.html')
# Ventas
@app.route('/ventas')
def ventas():
    return render_template('ventas.html')
if __name__ == '__main__':
    app.run(debug=True)
