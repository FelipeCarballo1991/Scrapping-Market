from etl.extract.extract import extract


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Ejecuta el scrapper de precios")

    parser.add_argument("--export", action="store_true", help="Guardar archivo localmente")
    parser.add_argument("--csv", action="store_true", help="Guardar como CSV (si no, guarda en parquet)")
    parser.add_argument("--debug", action="store_true", help="Usar URLs de prueba")
    parser.add_argument("--categoria", type=str, help="Filtrar por categoría específica")
    parser.add_argument("--drive", action="store_true", help="Subir a Google Sheets")

    args = parser.parse_args()

    extract(
        debug_export=args.export,
        debug_format=args.csv,
        debug_info=args.debug,
        categoria=args.categoria,
        debug_drive=args.drive
    )


    #     extract(
    #     debug_export=False,        # Guardar localmente
    #     debug_format=True,        # CSV
    #     debug_info=False,         # URLs reales o debug
    #     # categoria="Limpiezas",    # Filtro opcional
    #     debug_drive=True          # Subida a Google Sheet
    # )
