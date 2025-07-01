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


def subir_df_a_google_sheet(df, nombre_hoja, folder_id, ruta_credenciales, nombre_worksheet='Sheet1', limpiar_worksheets=False):
    from gspread_dataframe import set_with_dataframe
    import gspread
    from oauth2client.service_account import ServiceAccountCredentials
    from googleapiclient.discovery import build

    try:
        scope = [
            "https://spreadsheets.google.com/feeds",
            "https://www.googleapis.com/auth/drive"
        ]
        credentials = ServiceAccountCredentials.from_json_keyfile_name(ruta_credenciales, scope)
        gc = gspread.authorize(credentials)
        service = build('drive', 'v3', credentials=credentials)

        # Buscar hoja existente o crear nueva
        creado = False
        try:
            spreadsheet = gc.open(nombre_hoja)
            print("⚠️ La hoja ya existía, se actualizará.")
        except gspread.SpreadsheetNotFound:
            spreadsheet = gc.create(nombre_hoja)
            print("✅ Hoja creada.")
            creado = True

        # 🔁 Mover el archivo siempre al folder deseado
        try:
            file = service.files().get(fileId=spreadsheet.id, fields='parents').execute()
            previous_parents = ",".join(file.get('parents', []))
            if previous_parents != folder_id:
                service.files().update(
                    fileId=spreadsheet.id,
                    addParents=folder_id,
                    removeParents=previous_parents if previous_parents else '',
                    fields='id, parents'
                ).execute()
                print("📁 Archivo movido a la carpeta indicada.")
        except Exception as e:
            print(f"⚠️ No se pudo mover a la carpeta: {e}")

        # 🧹 Limpiar worksheets no deseados
        if limpiar_worksheets:
            hojas_deseadas = [nombre_worksheet]
            for ws in spreadsheet.worksheets():
                if ws.title not in hojas_deseadas:
                    spreadsheet.del_worksheet(ws)
                    print(f"🗑️ Worksheet '{ws.title}' eliminado.")

        # Seleccionar o crear worksheet específico
        try:
            worksheet = spreadsheet.worksheet(nombre_worksheet)
            print(f"✏️ Actualizando worksheet: {nombre_worksheet}")
            worksheet.clear()
        except gspread.WorksheetNotFound:
            worksheet = spreadsheet.add_worksheet(title=nombre_worksheet, rows=str(len(df)+10), cols=str(len(df.columns)+5))
            print(f"📄 Worksheet '{nombre_worksheet}' creado.")

        # Subir DataFrame
        set_with_dataframe(worksheet, df)
        print(f"📤 Subido a worksheet '{nombre_worksheet}' en: https://docs.google.com/spreadsheets/d/{spreadsheet.id}")

    except Exception as e:
        print(f"❌ Error al cargar al Drive. Error: {e}")




# Ejecución
if __name__ == "__main__":
    ...
