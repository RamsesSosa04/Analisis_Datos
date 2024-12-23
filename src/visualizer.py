import matplotlib.pyplot as plt

def show_histogram(data, column, title = "histograma"):
    try:
        plt.hist(data[column], bins=10, color="blue", alpha=0.7)
        plt.title(title)
        plt.xlabel(column)
        plt.ylabel("Frecuencia")
        plt.show()
    
    except Exception as e:
        print(f"Error al generar el grafico: {e}")
        raise