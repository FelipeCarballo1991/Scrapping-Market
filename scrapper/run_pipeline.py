from etl.extract.extract import extract

if __name__ == "__main__":
    extract(
        debug_export=False,        # Guardar localmente
        debug_format=True,        # CSV
        debug_info=False,         # URLs reales o debug
        # categoria="Limpiezas",    # Filtro opcional
        debug_drive=True          # Subida a Google Sheet
    )
