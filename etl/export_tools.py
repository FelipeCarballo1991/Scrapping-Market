import os
import gspread
from gspread_dataframe import set_with_dataframe
from googleapiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials


def guardar_localmente(df, path, formato_csv=True):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    if formato_csv:
        df.to_csv(path, mode='w', index=False, header=True, encoding="utf-8-sig")
    else:
        df.to_parquet(path, index=False)
    print(f"✅ Archivo guardado en: {os.path.abspath(path)}")


def subir_df_a_google_sheet(df, nombre_hoja, folder_id, ruta_credenciales):
    # Autenticación
    scope = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/drive"
    ]
    credentials = ServiceAccountCredentials.from_json_keyfile_name(ruta_credenciales, scope)
    gc = gspread.authorize(credentials)

    # Buscar hoja existente o crear nueva
    try:
        spreadsheet = gc.open(nombre_hoja)
        print("⚠️ La hoja ya existía, se actualizará.")
    except gspread.SpreadsheetNotFound:
        spreadsheet = gc.create(nombre_hoja)
        print("✅ Hoja creada.")

        # Mover a carpeta de Drive
        service = build('drive', 'v3', credentials=credentials)
        file = service.files().get(fileId=spreadsheet.id, fields='parents').execute()
        previous_parents = ",".join(file.get('parents'))
        service.files().update(
            fileId=spreadsheet.id,
            addParents=folder_id,
            removeParents=previous_parents,
            fields='id, parents'
        ).execute()

    # Subir DataFrame
    worksheet = spreadsheet.sheet1
    worksheet.clear()
    set_with_dataframe(worksheet, df)
    print(f"📤 Subido a Google Sheet: https://docs.google.com/spreadsheets/d/{spreadsheet.id}")
