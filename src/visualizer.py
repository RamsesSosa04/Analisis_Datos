import plotly.express as px

def generate_graphs(data):
    # Gráfico de goles por equipo
    fig = px.bar(data, x="Equipo", y="Goles", title="Goles por Equipo")
    graph_html = fig.to_html(full_html=False)
    return graph_html
