import sys
import os
import pandas as pd
from datetime import datetime
from playwright.sync_api import sync_playwright

# Ajuste del path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from config.urls import URLS, FECHA, FECHA_COMPLETA, URLS_DEBUG
# from config.folder import FOLDER_ID

# Prioridad 1: variable de entorno (GitHub Actions)
# Prioridad 2: importar desde archivo local si existe (tu PC)
try:
    FOLDER_ID = os.environ["DRIVE_FOLDER_ID"]
except KeyError:
    try:
        from config.folder import FOLDER_ID
    except ImportError:
        raise Exception("❌ No se encontró FOLDER_ID ni como variable de entorno ni en folder.py")



from etl.load.load import guardar_localmente, subir_df_a_google_sheet
from etl.transform.transform import generar_metricas




# Rutas
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Crear carpetas necesarias si no existen
os.makedirs(os.path.join(BASE_DIR, "..", "data", "raw"), exist_ok=True)
os.makedirs(os.path.join(BASE_DIR, "..", "logs"), exist_ok=True)

CSV_PATH = os.path.join(BASE_DIR, "..", "data", "raw", f"Precios_{FECHA}.csv")
PARQUET_PATH = os.path.join(BASE_DIR, "..", "data", "raw", f"Precios_{FECHA}.parquet")
LOG_PATH_ERROR = os.path.join(BASE_DIR, "..", "logs", "error_log.txt")
LOG_PATH_WARNING = os.path.join(BASE_DIR, "..", "logs", "error_warning.txt")

# Logging
def log_warning(msg):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_PATH_WARNING, "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] [WARNING] {msg}\n")

def log_error(msg):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_PATH_ERROR, "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] {msg}\n")

# Filtro por categoría
def filtrar_por_categoria(url, categoria):
    filtrados = {k: v for k, v in url.items() if v['categoria'] == categoria}
    if filtrados:
        return filtrados
    else:
        print("⚠️ No se encontraron productos en la categoría:", categoria)
        sys.exit(1)

# Scraping individual
def obtener_precio(page, url):
    try:
        page.goto(url, timeout=60000)
        titulo = None
        selectores_titulo = [
            'h2.title.text-dark',
            'h1.vtex-store-components-3-x-productNameContainer',
            'span.vtex-store-components-3-x-productBrand.vtex-store-components-3-x-productBrand--productNamePdp',
            'span.vtex-store-components-3-x-productBrand ',
            'span.vtex-store-components-3-x-productBrand.vtex-store-components-3-x-productBrand--quickview'
        ]
        for selector in selectores_titulo:
            try:
                page.wait_for_selector(selector, timeout=10000)
                titulo = page.query_selector(selector).inner_text().strip()
                break
            except:
                continue

        if not titulo:
            log_error(f"[ERROR] No se encontró el título en {url}")
            return None, None

        texto_estado = page.inner_text('body')
        if "Producto no disponible por el momento" in texto_estado:
            log_warning(f"[INFO] Producto no disponible: {titulo} – {url}")
            return titulo, None

        precio_raw = None
        selectores_posibles = [
            'var.price.h3.ng-star-inserted',
            'var.price.h3',
            'div.mb-1 var.price.h3',
            'div.mb-1 var',
            'price h3',
            "span.diaio-store-5-x-sellingPriceValue",
            'div.vtex-price-format-gallery',
            "span[class*='product-price-0-x-currencyContainer']"
        ]
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
            log_error(f"[ERROR] No se encontró el precio en {url} con los selectores: {selectores_posibles}")
            return titulo, None

        precio = float(precio_raw.replace("$", "").replace(".", "").replace(",", "."))
        return titulo, precio

    except Exception as e:
        log_error(f"Error al scrapear {url}: {e}")
        return None, None



# Función principal
def extract(debug_export=True, debug_format=False, debug_info=False, categoria=None, debug_drive=False):
    print("-----------------INICIO DE EJECUCION SCRAPPER MARKET----------------------")
    print(f"⏳ EJECUCION DEL DIA: {FECHA}")
    print(f"⏳ INICIO DE EJECUCION: {datetime.now().strftime('%H:%M:%S')}")
    print("--------------------------------------------------------------------------")

    PATH = CSV_PATH if debug_format else PARQUET_PATH
    urls_a_usar = URLS_DEBUG if debug_info else URLS

    if categoria:
        print(f"📏 Filtramos por categoria {categoria}")
        urls_a_usar = filtrar_por_categoria(URLS, categoria)

    resultados = []
    
    with sync_playwright() as p:
        
        try:
            # headless = os.environ.get("HEADLESS", "true").lower() == "true"
            browser = p.chromium.launch(headless=True)
        
        except:
            browser = p.chromium.launch(headless=False, args=[
            "--window-position=-32000,-32000",
            "--window-size=800,600",
            "--disable-infobars",
            "--no-sandbox",
            "--disable-gpu"
            ])
        
            

       
        page = browser.new_page()
        page.evaluate("""() => {
            Object.defineProperty(navigator, 'webdriver', { get: () => undefined });
        }""")

        for clave, datos in urls_a_usar.items():
            print(f"🔍 Procesando {datos['nombre']}")
            for supermercado, url in datos["urls"].items():
                print(f"    - En Supermercado {supermercado}...")
                nombre, precio = obtener_precio(page, url)
                if nombre and precio:
                    resultados.append([
                        FECHA, datos["nombre"], nombre, precio, datos["unidad"], supermercado, datos["categoria"], url
                    ])
                else:
                    log_error(f"[ERROR] No se pudo obtener el precio para: {datos['nombre']} | {url}")
        browser.close()

    
    try:
        df = pd.DataFrame(resultados, columns=[
        "fecha", "clave_config", "titulo_scrapeado", "precio", "unidad", "supermercado", "categoria", "url"
        ])
        print(f"Cantidad de productos scrapeados: {df['clave_config'].nunique()}")
        print("📏 Generando métricas particulares...")
        df = generar_metricas(df)
        print("✅ Métricas generadas")
    except Exception as e:
        print(f"No se pudo generar las metricas. Error: {e}")
        log_error(f"No se pudo generar las metricas. Error: {e}")
        sys.exit(1)

    

    if debug_export:
        guardar_localmente(df, PATH, formato_csv=debug_format)

    if debug_drive:
        nombre_hoja = f"Precios_{FECHA_COMPLETA}"
        ruta_credenciales = os.path.join(os.path.dirname(__file__), "credentials.json")
        subir_df_a_google_sheet(df, nombre_hoja, FOLDER_ID, ruta_credenciales)

    print("--------------------------------------------------------------------------")
    print(f"⏳ FIN DE EJECUCION: {datetime.now().strftime('%H:%M:%S')}")

# Ejecución
if __name__ == "__main__":
    extract(
        debug_export=True,
        debug_format=True,
        debug_info=False,
        categoria="Limpiezas",
        debug_drive=True
    )
