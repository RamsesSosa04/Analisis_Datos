from data_loader import load_csv
from stats_calculator import calculate_statistics
from visualizer import show_histogram

def main():
    """
    Función principal que coordina el flujo del proyecto.
    """
    try:
        # Paso 1: Cargar datos
        file_path = input("Ingresa la ruta del archivo CSV: ")
        data = load_csv(file_path)

        # Paso 2: Calcular estadísticas
        stats = calculate_statistics(data)
        print("Estadísticas calculadas:")
        for key, value in stats.items():
            print(f"{key}: {value}")

        # Paso 3: Visualizar estadísticas
        column = input("Ingresa la columna que deseas visualizar (por ejemplo, GolesLocal): ")
        show_histogram(data, column, f"Distribución de {column}")

    except Exception as e:
        print(f"Error en la aplicación: {e}")

if __name__ == "__main__":
    main()
