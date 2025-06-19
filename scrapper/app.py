
import sys
import os
import pandas as pd
from datetime import datetime
from playwright.sync_api import sync_playwright
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from config.urls import URLS,FECHA,URLS_DEBUG


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_PATH = os.path.join(BASE_DIR, "..", "data", "raw", f"Precios_{FECHA}.csv")
PARQUET_PATH = os.path.join(BASE_DIR, "..", "data", "raw", f"Precios_{FECHA}.parquet")
LOG_PATH_ERROR = os.path.join(BASE_DIR, "..", "logs", "error_log.txt")
LOG_PATH_WARNING = os.path.join(BASE_DIR, "..", "logs", "error_warning.txt")


os.makedirs(os.path.dirname(CSV_PATH), exist_ok=True)
os.makedirs(os.path.dirname(PARQUET_PATH), exist_ok=True)
os.makedirs(os.path.dirname(LOG_PATH_ERROR), exist_ok=True)

def log_warning(msg):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_PATH_WARNING, "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] [WARNING] {msg}\n")

def log_error(msg):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_PATH_ERROR, "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] {msg}\n")


def filtrar_por_categoria(url, categoria):
    filtrados = {k: v for k, v in url.items() if v['categoria'] == categoria}
    if filtrados:
        return filtrados
    else:
        print("⚠️ No se encontraron productos en la categoría:", categoria)
        sys.exit(1)


def obtener_precio(page, url):
    try:
        page.goto(url, timeout=60000)       

        # html = page.content()
        # # breakpoint()
        # with open("debug_dia.html", "w", encoding="utf-8") as f:
        #     f.write(html)
        
        # breakpoint()
        # Selectores posibles para el título (Coto, Dia, etc.)
        titulo = None
        selectores_titulo = [
            'h2.title.text-dark',  # Coto
            'h1.vtex-store-components-3-x-productNameContainer',            
            'span.vtex-store-components-3-x-productBrand.vtex-store-components-3-x-productBrand--productNamePdp',
            'span.vtex-store-components-3-x-productBrand ',
            'span.vtex-store-components-3-x-productBrand.vtex-store-components-3-x-productBrand--quickview' 
        ]

        for selector in selectores_titulo:
            try:
                page.wait_for_selector(selector, timeout=10000)
                titulo = page.query_selector(selector).inner_text().strip()
                # breakpoint()
                break
            except:
                continue

        if not titulo:
            log_error(f"[ERROR] No se encontró el título en {url}")          
            
            return None, None

        # Verificar si el producto está disponible
        texto_estado = page.inner_text('body')
        if "Producto no disponible por el momento" in texto_estado:
            log_warning(f"[INFO] Producto no disponible: {titulo} – {url}")
            return titulo, None

        # Intentar varios selectores para el precio
        precio_raw = None
        selectores_posibles = [
            'var.price.h3.ng-star-inserted',
            'var.price.h3', 
            'div.mb-1 var.price.h3',          
            'div.mb-1 var',
            'price h3',            
            "span.diaio-store-5-x-sellingPriceValue",
            # 'div.jumboargentinaio-store-theme-2t-mVsKNpKjmCAEM_AMCQH'
            'div.vtex-price-format-gallery',
            "span[class*='product-price-0-x-currencyContainer']"  # Para Carrefour
        ]

        # breakpoint()

        for selector in selectores_posibles:
            try:
                page.wait_for_selector(selector, timeout=10000)

                if "currencyContainer" in selector:
                    span_container = page.query_selector(selector)
                    span_elements = span_container.query_selector_all("span")
                    precio_raw = ''.join([s.inner_text().strip() for s in span_elements]).replace("\u00a0", "")                   

                else:
                    precio_raw = page.query_selector(selector).inner_text().strip()
                
                break
            except:
                continue

        if not precio_raw:
            # Solo logueamos error si ninguno funcionó
            log_error(f"[ERROR] No se encontró el precio en {url} con ninguno de los selectores: {selectores_posibles}")
            return titulo, None

        # Limpieza del precio
        precio = float(precio_raw.replace("$", "").replace(".", "").replace(",", "."))       

        return titulo, precio

    except Exception as e:
        # breakpoint()
        log_error(f"Error al scrapear {url}: {e}")
        return None, None


def generar_metricas(df):

    try:
        
        df[['cant_unidades', 'largo_mts']] = df['unidad'].str.extract(r'(\d+)\s+Unidades\s+x\s+(\d+)\s+mts')    
        df['cant_unidades'] = df['cant_unidades'].apply(lambda x: int(x) if pd.notna(x) else x)
        df['largo_mts'] = df['largo_mts'].apply(lambda x: int(x) if pd.notna(x) else x)
        df["precio_rollo"] = round(df["precio"] / df["cant_unidades"],2)
        df["precio_metro"] = round(df["precio_rollo"]/ df["largo_mts"],2)
    
    except Exception as e:
            log_warning(f"[INFO] Error la generar la metrica: {e}")

def trackear_precios(debug_format = False, debug_info = False, categoria = None):

    PATH = CSV_PATH if debug_format else PARQUET_PATH
    urls_a_usar = URLS_DEBUG if debug_info else URLS  

    if categoria != None:
        urls_a_usar = filtrar_por_categoria(URLS,categoria)
      

    resultados = []    

    with sync_playwright() as p:

        browser = p.chromium.launch(
                                headless=False,
                                args=[
                                    "--window-position=-32000,-32000",  # Mueve la ventana fuera de la pantalla
                                    "--window-size=800,600",            # Tamaño mínimo
                                    "--disable-infobars",
                                    "--no-sandbox",
                                    "--disable-gpu"
                                ]
                            )       
        
        page = browser.new_page()

        page.evaluate("""
                        () => {
                            Object.defineProperty(navigator, 'webdriver', { get: () => undefined });
                        }
                      """)

        for clave, datos in urls_a_usar.items():
            nombre_config = datos["nombre"]           
            unidad = datos["unidad"]
            categoria = datos["categoria"]
            print(f"🔍 Procesando {nombre_config}")

            for supermercado, url in datos["urls"].items():
                print(f"    -En Supermercado {supermercado}...")

                
                nombre, precio = obtener_precio(page, url)

                if nombre and precio:
                    resultados.append([
                        FECHA, nombre_config, nombre, precio, unidad, supermercado, categoria, url
                    ])
                else:
                    log_error(f"No se pudo obtener el precio para: {nombre_config} | {url}")

        browser.close()

# breakpoint()

    

    # Crear un DataFrame
    df = pd.DataFrame(resultados, columns=[
        "fecha", "clave_config", "titulo_scrapeado", "precio", "unidad", "supermercado", "categoria","url"
    ])

    # breakpoint()

    # Guardar el DataFrame
    if not os.path.exists(PATH):

        if debug_format:                 
            df.to_csv(PATH, mode='w', index=False, header=True, encoding="utf-8-sig")
        else:
            df.to_parquet(PATH, index=False)

    else:
        pass

    cantidad_productos = int(df[['clave_config']].nunique().iloc[0])

    print(f"Cantidad de productos scrapeados: {cantidad_productos}")

    print("📏 Generando métricas particulares...")
    df = generar_metricas(df)
    print("✅ Métricas generadas")


    print(f"✅ Precios guardados en: {os.path.abspath(PATH)}")
    



if __name__ == "__main__":
    trackear_precios(debug_format = True,
                     debug_info = False,
                    #  categoria = "Limpiezas"
                     )
