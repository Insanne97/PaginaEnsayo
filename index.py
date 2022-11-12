from flask import Flask, render_template #Llamamos a flask

app = Flask(__name__) #Obtenemos un obejeto llamado app

@app.route('/') #Creamos una ruta para Home
def home():
    return render_template('home.html')

@app.route('/about') #Creamos una ruta para About
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)