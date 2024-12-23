from flask import Flask, render_template, request
from src.data_loader import load_csv
from src.stats_calculator import calculate_statistics
import os

app = Flask(__name__)

@app.route('/')
def index():
    """
    Página principal con la interfaz gráfica.
    """
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    """
    Procesa el archivo CSV subido por el usuario.
    """
    if 'file' not in request.files:
        return "No se subió ningún archivo."
    
    file = request.files['file']
    
    if file.filename == '':
        return "El archivo no tiene nombre."
    
    if file:
        # Guardar el archivo en la carpeta "Data"
        file_path = os.path.join('Data', file.filename)
        file.save(file_path)

        # Cargar y validar datos
        try:
            data = load_csv(file_path)
            stats = calculate_statistics(data)
            return render_template('index.html', stats=stats, filename=file.filename)
        except Exception as e:
            return f"Error procesando el archivo: {e}"

if __name__ == '__main__':
    app.run(debug=True)
