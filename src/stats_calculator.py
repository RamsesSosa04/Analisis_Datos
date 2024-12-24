import pandas as pd

def calculate_statistics(data):

    stats = {
        "Equipo Local": data["HomeTeam"],
        "Equipo Visitante": data["AwayTeam"],
        "Promedio de Goles Local": data["FTHG"].mean(),
        "Promedio de Goles Visita": data["FTAG"].mean()

    }
    return stats

def calculate_probabilities(data):
    # Cálculo probabilístico simple (ejemplo)
    probabilities = {
        "Promedio goles local": (data["Goles local"]).mean(),
        "Promedio goles visita": (data["Goles visita"]).mean(),
    }
    return probabilities