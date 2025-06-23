from etl.extract.extract import extract

if __name__ == "__main__":
    extract(
        debug_export=True,        # Guardar localmente
        debug_format=True,        # CSV
        debug_info=True,         # URLs reales o debug
        # categoria="Limpiezas",    # Filtro opcional
        debug_drive=False          # Subida a Google Sheet
    )
