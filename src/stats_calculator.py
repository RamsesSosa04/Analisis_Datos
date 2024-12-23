def calculate_statistics(data):

    try:
        stats = {
            "Equipo Local": data["HomeTeam"],
            "Equipo Visitante": data["AwayTeam"],
            "Promedio de Goles Local": data["FTHG"].mean(),
            "Promedio de Goles Visita": data["FTAG"].mean()

        }
        return stats
    
    except Exception as e:
        print(f"Error al calacular estadisticas: {e}")
        raise