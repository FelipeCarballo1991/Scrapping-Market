import gspread
import os
import sys
from oauth2client.service_account import ServiceAccountCredentials
from googleapiclient.discovery import build
from gspread_dataframe import set_with_dataframe

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from config.folder import FOLDER_ID


def obtener_hoja_existente(gc, nombre_hoja):
    hojas = gc.list_spreadsheet_files()
    for hoja in hojas:
        if hoja['name'] == nombre_hoja:
            return hoja
    return None  



def load(df,nombre_hoja):
    # Scope de acceso a Sheets y Drive
    scope = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/drive"
    ]

    # Autenticación con credenciales
    ruta_credenciales = os.path.join(os.path.dirname(__file__), "credentials.json")
    credentials = ServiceAccountCredentials.from_json_keyfile_name(ruta_credenciales, scope)
    gc = gspread.authorize(credentials)



    # spreadsheet = obtener_hoja_existente(gc, nombre_hoja)

    hoja_existente = obtener_hoja_existente(gc, nombre_hoja)
    if hoja_existente:
        spreadsheet = gc.open_by_key(hoja_existente['id'])
        print("⚠️ La hoja ya existe.")
    else:
        spreadsheet = gc.create(nombre_hoja)
        print("✅ Hoja creada")


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

    worksheet.clear()  # Limpia la hoja (opcional)
    set_with_dataframe(worksheet, df)
    print("⬆️ DataFrame cargado con éxito en Google Sheets.")



if __name__ == "__main__":

    import pandas as pd

    # Crear un DataFrame de ejemplo
    df = pd.DataFrame({
        "Producto": ["Manzana", "Brócoli", "Zanahoria"],
        "Precio": [120, 340, 200]
    })

    nombre_hoja = "Mi Nueva Hoja desde Python2"
    load(df,nombre_hoja)

    

