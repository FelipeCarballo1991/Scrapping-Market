# from etl.extract.extract import log_warning
import pandas as pd

# Métricas
def generar_metricas(df):    

    df = df[['fecha', 
            'clave_config', 
            'titulo_scrapeado', 
            'precio', 
            'unidad',
            'supermercado', 
            'categoria',    
            'cant_unidades', 
            'largo_mts',
            'precio_rollo', 
            'precio_metro',
            'url', ]]

    df[['cant_unidades', 'largo_mts']] = df['unidad'].str.extract(r'(\d+)\s+Unidades\s+x\s+(\d+)\s+mts')
    df['cant_unidades'] = df['cant_unidades'].apply(lambda x: int(x) if pd.notna(x) else x)
    df['largo_mts'] = df['largo_mts'].apply(lambda x: int(x) if pd.notna(x) else x)
    df["precio_rollo"] = round(df["precio"] / df["cant_unidades"], 2)
    df["precio_metro"] = round(df["precio_rollo"] / df["largo_mts"], 2)   


     
        
    return df


# Ejecución
if __name__ == "__main__":
    ...