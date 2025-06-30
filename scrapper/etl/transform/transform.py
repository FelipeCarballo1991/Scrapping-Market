# from etl.extract.extract import log_warning
import pandas as pd

# Métricas
def generar_metricas(df):     

    #METRICAS PAPEL HIGIENICO
    df[['cant_unidades', 'largo_mts']] = df['unidad'].str.extract(r'(\d+)\s+Unidades\s+x\s+(\d+)\s+mts')
    df['cant_unidades'] = df['cant_unidades'].apply(lambda x: int(x) if pd.notna(x) else x)
    df['largo_mts'] = df['largo_mts'].apply(lambda x: int(x) if pd.notna(x) else x)
    df["precio_rollo"] = round(df["precio"] / df["cant_unidades"], 2)
    df["precio_metro"] = round(df["precio_rollo"] / df["largo_mts"], 2)

    # METRICAS PAPEL DE COCINA
    df[['cant_unidades_rollo', 'cant_panio']] = df['unidad'].str.extract(r'(\d+)\s+Unidades\s+x\s+(\d+)\s+panios')
    df['cant_unidades_rollo'] = df['cant_unidades_rollo'].apply(lambda x: int(x) if pd.notna(x) else x)
    df['cant_panio'] = df['cant_panio'].apply(lambda x: int(x) if pd.notna(x) else x)
    df["precio_rollo_cocina"] = round(df["precio"] / df["cant_unidades_rollo"], 2)
    df["precio_panio_cocina"] = round(df["precio_rollo_cocina"] / df["cant_panio"], 2)   

    # METRICAS DEMAS CATEGORIAS
    df['Unidad_num'] = pd.to_numeric(df['unidad'], errors='coerce')
    # Calcular el precio por unidad sólo para los valores numéricos
    df['precio_por_unidad'] = round(df['precio'] / df['Unidad_num'],2)



    df = df[['fecha', 
            'clave_config', 
            'titulo_scrapeado', 
            'precio', 
            'unidad',
            'precio_por_unidad',
            'precio_metro',
            'precio_panio_cocina',
            'supermercado', 
            'categoria',    
            # 'cant_unidades', 
            # 'largo_mts',
            # 'precio_rollo', 
            # 'precio_metro',
            # 'cant_unidades_rollo',
            # 'cant_panio',
            # 'precio_rollo_cocina',
            # 'precio_panio_cocina'
            'url', ]]
     
        
    return df


# Ejecución
if __name__ == "__main__":
    ...