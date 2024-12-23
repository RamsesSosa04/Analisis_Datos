import pandas as pd

def load_csv(file_path):
    try: 
        data = pd.read_csv(file_path)

        required_columns =["Date","HomeTeam","AwayTeam","FTHG","FTAG","FTR","HTHG","HTAG","HTR","Referee","HS","AS","HST","AST","HF","AF","HC","AC","HY","AY","HR","AR"]

        for col in required_columns:
            if col not in data.columns:
                raise ValueError(f"La columna '{col}' no esta presente en el archivo")
            
            print("Archivo CSV cargado correctamente.")
            return data
    except Exception as e:
        print(f"Error al cargar el archivo CSV: {e}")
        raise