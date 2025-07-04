# 🛒 Scrapping-Market

Este proyecto automatiza la recolección diaria de precios de productos desde distintas URLs de supermercados utilizando **Playwright**. Los datos son transformados con **Pandas** y almacenados localmente o en **Google Drive** mediante la API de Google. Todo el proceso se orquesta mediante **GitHub Actions**, funcionando como un pipeline ETL diario.

---

## ⚙️ Tecnologías utilizadas

- **Python**
- **Playwright** (`playwright.sync_api`)
- **Pandas**
- **Google Sheets API + Drive API**
- **gspread + oauth2client**
- **GitHub Actions**
- **dotenv** para manejo de variables de entorno

---

## 🚀 ¿Qué hace?

1. **Extract**: Realiza scraping sobre múltiples URLs para extraer título y precio.
2. **Transform**: Calcula métricas como `precio_rollo` y `precio_metro` a partir de los datos.
3. **Load**:
   - Guarda los datos en `.csv` o `.parquet`.
   - Opcionalmente los sube automáticamente a Google Sheets dentro de una carpeta de Google Drive.
4. **Automatización**: Ejecutado diariamente a través de GitHub Actions en horas de la mañana.

## 🧪 Ejecución manual

Desde la raíz del proyecto:

```bash
python scrapper/run_pipeline.py [OPCIONES]
```

| Flag          | Descripción                                                                    |
| ------------- | ------------------------------------------------------------------------------ |
| `--export`    | Guarda el archivo localmente (por defecto en `/data/raw`)                      |
| `--csv`       | Guarda en formato `.csv` (por defecto `.parquet` si no se especifica)          |
| `--debug`     | Usa URLs de prueba definidas en `URLS_DEBUG`                                   |
| `--categoria` | Filtra la ejecución por una categoría específica (ej: `--categoria Limpiezas`) |
| `--drive`     | Sube el resultado a Google Sheets dentro de la carpeta indicada                |
