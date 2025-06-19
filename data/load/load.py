import gspread
import os
import sys
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials
from googleapiclient.discovery import build
from gspread_dataframe import set_with_dataframe

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from config.folder import FOLDER_ID

# Scope de acceso a Sheets y Drive
scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive"
]

def obtener_hoja_existente(gc, nombre_hoja):
    try:
        return gc.open(nombre_hoja)  # Intenta abrir una hoja con ese nombre
    except gspread.SpreadsheetNotFound:
        return None

# Autenticación con credenciales
ruta_credenciales = os.path.join(os.path.dirname(__file__), "credentials.json")
credentials = ServiceAccountCredentials.from_json_keyfile_name(ruta_credenciales, scope)
gc = gspread.authorize(credentials)

nombre_hoja = "Mi Nueva Hoja desde Python"

spreadsheet = obtener_hoja_existente(gc, nombre_hoja)

if spreadsheet is None:
    spreadsheet = gc.create(nombre_hoja)
    print("✅ Hoja creada")
else:
    print("⚠️ La Hoja ya existe, no se volvió a crear")


spreadsheet_id = spreadsheet.id

# Crear cliente de Google Drive
drive_service = build('drive', 'v3', credentials=credentials)

# Obtener padres actuales (carpeta temporal)
file = drive_service.files().get(fileId=spreadsheet_id, fields='parents').execute()
previous_parents = ",".join(file.get('parents'))

# Mover el archivo a la carpeta deseada
drive_service.files().update(
    fileId=spreadsheet_id,
    addParents=FOLDER_ID,
    removeParents=previous_parents,
    fields='id, parents'
).execute()

# Acceder a la hoja y escribir un mensaje
worksheet = spreadsheet.sheet1

# Crear un DataFrame de ejemplo
df = pd.DataFrame({
    "Producto": ["Manzana", "Brócoli", "Zanahoria"],
    "Precio": [120, 340, 200]
})

worksheet.clear()  # Limpia la hoja (opcional)
set_with_dataframe(worksheet, df)
print("⬆️ DataFrame cargado con éxito en Google Sheets.")


