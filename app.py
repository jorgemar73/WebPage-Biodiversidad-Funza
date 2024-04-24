from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit_contact', methods=['POST'])
def submit_contact():
    # Aquí puedes agregar la lógica para manejar el formulario enviado
    return 'Gracias por contactarnos'

if __name__ == '__main__':
    app.run(debug=True)
