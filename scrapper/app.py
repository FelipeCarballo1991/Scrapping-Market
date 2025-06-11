
import sys
import os
import pandas as pd
from datetime import datetime
from playwright.sync_api import sync_playwright
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from config.urls import URLS # <- Importa directamente desde config/urls.py


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_PATH = os.path.join(BASE_DIR, "..", "data", "processed", "precios_coto.csv")
LOG_PATH = os.path.join(BASE_DIR, "..", "logs", "error_log.txt")


os.makedirs(os.path.dirname(CSV_PATH), exist_ok=True)
os.makedirs(os.path.dirname(LOG_PATH), exist_ok=True)


def log_error(msg):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_PATH, "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] {msg}\n")


def obtener_precio(page, url):
    try:
        page.goto(url, timeout=60000)
        page.wait_for_selector('h2.title.text-dark', timeout=15000)
        # page.wait_for_selector('var.price.h3.ng-star-inserted', timeout=15000) 

        # price h3 ng-star-inserted

        titulo = page.query_selector('h2.title.text-dark').inner_text().strip()
        # precio_raw = page.query_selector('var.price.h3.ng-star-inserted').inner_text().strip()

        # Intentar varios selectores para el precio
        precio_raw = None
        selectores_posibles = [
            'var.price.h3.ng-star-inserted',
            'var.price.h3',
            'div.mb-1 var'
        ]

        for selector in selectores_posibles:
            try:
                page.wait_for_selector(selector, timeout=5000)
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


def trackear_precios():
    resultados = []
    fecha = datetime.now().strftime("%Y-%m-%d")

    with sync_playwright() as p:

        browser = p.chromium.launch(
                                headless=False,
                                # args=[
                                #     "--window-position=-32000,-32000",  # Mueve la ventana fuera de la pantalla
                                #     "--window-size=800,600",            # Tamaño mínimo
                                #     "--disable-infobars",
                                #     "--no-sandbox",
                                #     "--disable-gpu"
                                # ]
                            )
        # browser = p.chromium.launch(headless=True,
        #                              args=[
        #                                     "--disable-blink-features=AutomationControlled",
        #                                     "--disable-gpu",
        #                                     "--no-sandbox",
        #                                     "--disable-dev-shm-usage",
        #                                     "--disable-infobars",
        #                                     "--window-size=1920,1080",
        #                                 ])
        
        page = browser.new_page()

        page.evaluate("""
            () => {
                Object.defineProperty(navigator, 'webdriver', { get: () => undefined });
            }
        """)

        for clave, datos in URLS.items():
            nombre_config = datos["nombre"]
            url = datos["url"]
            supermercado = datos["supermercado"]
            unidad = datos["unidad"]
            categoria = datos["categoria"]

            print(f"🔍 Procesando {nombre_config}...")
            nombre, precio = obtener_precio(page, url)

            if nombre and precio:
                resultados.append([
                    fecha, nombre_config, nombre, precio, unidad, supermercado, url,categoria
                ])
            else:
                log_error(f"No se pudo obtener el precio para: {nombre_config} | {url}")

        browser.close()

# breakpoint()

    

    # Crear un DataFrame
    df = pd.DataFrame(resultados, columns=[
        "fecha", "clave_config", "titulo_scrapeado", "precio", "unidad", "supermercado", "url","categoria"
    ])

    # breakpoint()

    # Guardar el DataFrame
    if os.path.exists(CSV_PATH):
        df.to_csv(CSV_PATH, mode='a', index=False, header=False, encoding='utf-8')
    else:
        df.to_csv(CSV_PATH, mode='w', index=False, header=True, encoding='utf-8')


    print(f"✅ Precios guardados en: {os.path.abspath(CSV_PATH)}")



if __name__ == "__main__":
    trackear_precios()
