from flask import Flask, render_template, jsonify
import csv

app = Flask(__name__)

# Función para cargar partidos desde el archivo CSV
def load_matches_from_csv(file_path):
    leagues = {}
    try:
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                league = "Premier League"  # Cambia esto si tienes más ligas
                match = {
                    "Date": row['Date'],
                    "Equipo1": row['HomeTeam'],
                    "Equipo2": row['AwayTeam'],
                    "FTHG": row['FTHG'],  # Goles del equipo local
                    "FTAG": row['FTAG'],  # Goles del equipo visitante
                    "FTR": row['FTR'],    # Resultado final
                }
                if league not in leagues:
                    leagues[league] = []
                leagues[league].append(match)
        return leagues
    except Exception as e:
        print(f"Error al leer el archivo CSV: {e}")
        return {}

# Ruta al archivo CSV
MATCHES_FILE = 'matches.csv'
LEAGUES = load_matches_from_csv(MATCHES_FILE)

# Ruta principal
@app.route('/')
def index():
    return render_template('index.html', leagues=LEAGUES.keys())

# Ruta para obtener partidos de una liga específica
@app.route('/get_matches/<league>')
def get_matches(league):
    matches = LEAGUES.get(league, [])
    return jsonify(matches)

if __name__ == '__main__':
    app.run(debug=True)
