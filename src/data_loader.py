import pandas as pd

required_columns =["Date","HomeTeam","AwayTeam","FTHG","FTAG","FTR","HTHG","HTAG","HTR","Referee","HS","AS","HST","AST","HF","AF","HC","AC","HY","AY","HR","AR"]

def load_data(file):
    try:
        data = pd.read_csv(file)
        
        # Validar columnas requeridas
        missing_columns = [col for col in required_columns if col not in data.columns]
        if missing_columns:
            return None, f"Faltan las siguientes columnas: {', '.join(missing_columns)}"
        
        # Retornar los datos cargados
        return data, None
    except Exception as e:
        return None, f"Error al cargar los datos: {str(e)}"
