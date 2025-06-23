from datetime import datetime
import pandas as pd

FECHA = datetime.now().strftime("%Y-%m-%d")
FECHA_COMPLETA = datetime.now().strftime("%Y-%m-%d_%H:%M_%S")


URLS_DEBUG = {
     "brocoli": {
        "nombre": "Brocoli",        
        "unidad": "kg",        
        "categoria": "Verdura",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/brocoli-x-kg/_/R-00000598-00000598-200asdasd",
                }
}
}

URLS = {
    "bife_americano": {
        "nombre": "Bife Americano",        
        "unidad": "kg",        
        "categoria": "Carnes",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/bife-americano-x-kg/_/R-00041414-00041414-200?Dy=1",
                }
    },
    "ojo_bife": {
        "nombre": "Ojo de Bife",        
        "unidad": "kg",        
        "categoria": "Carnes",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/ojo-de-bife-coto-xkg/_/R-00029810-00029810-200?Dy=1",
                }
    },
    "bife_chorizo": {
        "nombre": "Bife de Chorizo",        
        "unidad": "kg",        
        "categoria": "Carnes",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/bife-de-chorizo-coto-xkg/_/R-00029804-00029804-200?Dy=1",
                }
    },    
    "cuadril": {
        "nombre": "Cuadril",        
        "unidad": "kg",        
        "categoria": "Carnes",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/cuadril-selecci%C3%B3n-x-kg/_/R-00042317-00042317-200?Dy=1",
                }
    },
        "picada_desgrasada": {
        "nombre": "Picada Desgrasada",        
        "unidad": "kg",        
        "categoria": "Carnes",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/picada-desgrasada-estancias-coto-x-kg/_/R-00048124-00048124-200?Dy=1",
                }
    },
        "bola_lomo": {
        "nombre": "Bola de Lomo",        
        "unidad": "kg",        
        "categoria": "Carnes",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/bola-de-lomo-estancias-coto-x-kg/_/R-00047993-00047993-200?Dy=1",
                }
    },
        "nalga": {
        "nombre": "Nalga",        
        "unidad": "kg",        
        "categoria": "Carnes",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/nalga-estancias-coto-x-kg/_/R-00047991-00047991-200?Dy=1&assemblerContentCollection=%2Fcontent%2FShared%2FAuto-Suggest%20Panels",
                }
    },
        "peceto": {
        "nombre": "Peceto",        
        "unidad": "kg",        
        "categoria": "Carnes",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/peceto-feteado-x-kg/_/R-00041407-00041407-200?Dy=1",
                }
    },
        "paleta": {
        "nombre": "Paleta",        
        "unidad": "kg",        
        "categoria": "Carnes",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/paleta-del-centro-estancias-coto-x-kg/_/R-00047984-00047984-200?Dy=1",
                }
    },
        "roast_beef": {
        "nombre": "Roast Beef",        
        "unidad": "kg",        
        "categoria": "Carnes",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/roast-beef-estancias-coto-x-kg/_/R-00047985-00047985-200?Dy=1&assemblerContentCollection=%2Fcontent%2FShared%2FAuto-Suggest%20Panels",
                }
    },
    
        "bife_parrilla": {
        "nombre": "Bife de Parrilla",        
        "unidad": "kg",        
        "categoria": "Carnes",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/bife-parrilla-estancias-coto-x-kg/_/R-00048129-00048129-200?Dy=1",
                }
    },    
        "pollo": {
        "nombre": "Pollo Entero",        
        "unidad": "kg",        
        "categoria": "Carnes",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/pollo-congelado-x-kg/_/R-00042989-00042989-200?Dy=1",
                }
    },
    "carre_cerdo": {
        "nombre": "Carre de Cerdo",        
        "unidad": "kg",        
        "categoria": "Carnes",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/carr%C3%A9-de-cerdo-x-kg/_/R-00017162-00017162-200?Dy=1",
                }
    },    
    "bondiola_cerdo": {
        "nombre": "Bondiola de Cerdo",        
        "unidad": "kg",        
        "categoria": "Carnes",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/bondiola-de-cerdo-x-kg/_/R-00000943-00000943-200?Dy=1&assemblerContentCollection=%2Fcontent%2FShared%2FAuto-Suggest%20Panels",
                }
    },     
        "papa_negra": {
        "nombre": "Papa Negra",        
        "unidad": "kg",        
        "categoria": "Verdura",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/papa-negra-selecci%C3%B3n-x-kg/_/R-00060947-00060947-200?Dy=1",
                }
    },    
        "cebolla": {
        "nombre": "Cebolla",        
        "unidad": "kg",        
        "categoria": "Verdura",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/cebolla-a-granel-x-kg/_/R-00000602-00000602-200?Dy=1",
                }
    },    
        "coliflor": {
        "nombre": "Coliflor",        
        "unidad": "kg",        
        "categoria": "Verdura",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/coliflor-x-kg/_/R-00000619-00000619-200?Dy=1",
                }
    },    
        "repollo_colorado": {
        "nombre": "Repollo Colorado",        
        "unidad": "kg",        
        "categoria": "Verdura",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/repollo-colorado-x-kg/_/R-00000680-00000680-200?Dy=1",
                }
    }, 
        "repollo_blanco": {
        "nombre": "Repollo Blanco",        
        "unidad": "kg",        
        "categoria": "Verdura",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/repollo-blanco-x-kg/_/R-00000678-00000678-200?Dy=1",
                }
    },    
        "zanahoria": {
        "nombre": "Zanahoria",        
        "unidad": "kg",        
        "categoria": "Verdura",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/zanahoria-seleccion-xkg/_/R-00000686-00000686-200?Dy=1",
                }
    },
      
        "perejil": {
        "nombre": "Perejil",        
        "unidad": "Unidad",        
        "categoria": "Verdura",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/perejil-x-uni/_/R-00047599-00047599-200?Dy=1",
                }
    },             
        "lechuga_mantecosa": {
        "nombre": "Lechuga Mantecosa",        
        "unidad": "kg",        
        "categoria": "Verdura",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/lechuga-mantecosa-x-kg/_/R-00000424-00000424-200?Dy=1",
                }
    }, 

        "lechuga_capuchina": {
        "nombre": "Lechuga Capuchina",        
        "unidad": "kg",        
        "categoria": "Verdura",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/lechuga-capuchina-x-kg/_/R-00000648-00000648-200?Dy=1",
                }   
    },             
        "lechuga_criolla": {
        "nombre": "Lechuga Criolla",        
        "unidad": "kg",        
        "categoria": "Verdura",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/lechuga-criolla-x-kg/_/R-00000649-00000649-200?Dy=1",
                }
    },             
        "lechuga_francesa": {
        "nombre": "Lechuga Francesa",        
        "unidad": "kg",        
        "categoria": "Verdura",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/lechuga-francesa-x-kg/_/R-00000650-00000650-200?Dy=1",
                }
    },             
        "brocoli": {
        "nombre": "Brocoli",        
        "unidad": "kg",        
        "categoria": "Verdura",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/brocoli-x-kg/_/R-00000598-00000598-200",
                }
    },             
        "jengibre": {
        "nombre": "Jengibre",        
        "unidad": "kg",        
        "categoria": "Verdura",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/jengibre-x-kg/_/R-00092926-00092926-200",
                }
    },             
        "pimiento_rojo": {
        "nombre": "Pimiento Rojo",        
        "unidad": "kg",        
        "categoria": "Verdura",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/pimiento-rojo-xkg/_/R-00000671-00000671-200?Dy=1",
                }
    },             
        "zapallo_anco": {
        "nombre": "Zapallo Anco",        
        "unidad": "kg",        
        "categoria": "Verdura",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/zapallo-anco-x-kg/_/R-00000688-00000688-200?Dy=1",
                }
    },             
        "remolacha": {
        "nombre": "Remolacha",        
        "unidad": "kg",        
        "categoria": "Verdura",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/remolacha-x-kg/_/R-00000677-00000677-200",
                }
    },             
        "tomate_redondo": {
        "nombre": "Tomate Redondo",        
        "unidad": "kg",        
        "categoria": "Verdura",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/tomate-red-x-kg/_/R-00000684-00000684-200?Dy=1&assemblerContentCollection=%2Fcontent%2FShared%2FAuto-Suggest%20Panels",
                }
    },             
        "tomate_perita": {
        "nombre": "Tomate Perita",        
        "unidad": "kg",        
        "categoria": "Verdura",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/tomate-perit-xkg/_/R-00000683-00000683-200?Dy=1&assemblerContentCollection=%2Fcontent%2FShared%2FAuto-Suggest%20Panels",
                }
    },                 
        "espinaca_granja_sol": {
        "nombre": "Espinaca granja del Sol",        
        "unidad": "kg",        
        "categoria": "Verdura",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/espinaca-congelada-granja-del-sol-1kg/_/R-00565167-00565167-200?Dy=1",
                }
    },                 
        "espinaca_lucchetti": {
        "nombre": "Espinaca Luchetti 400 gr",        
        "unidad": "gr",        
        "categoria": "Verdura",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/espinaca-congelada-lucchetti-400g/_/R-00565182-00565182-200?Dy=1",
                }
    },               
        "banana": {
        "nombre": "Banana",        
        "unidad": "kg",        
        "categoria": "Fruta",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/banana-cavendish-x-kg/_/R-00000446-00000446-200?Dy=1",
                }
    },             
        "naranja_jugo": {
        "nombre": "Naranja Jugo",        
        "unidad": "kg",        
        "categoria": "Fruta",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/naranja-jugo-xkg/_/R-00061005-00061005-200?Dy=1&assemblerContentCollection=%2Fcontent%2FShared%2FAuto-Suggest%20Panels",
                }
    },                 
        "uva_red_glove": {
        "nombre": "Uva Red Glove",        
        "unidad": "kg",        
        "categoria": "Fruta",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/uva-red-globe-xkg/_/R-00000861-00000861-200?Dy=1&assemblerContentCollection=%2Fcontent%2FShared%2FAuto-Suggest%20Panels",
                }
    },                     
        "manzana_roja": {
        "nombre": "Manzana Roja",        
        "unidad": "kg",        
        "categoria": "Fruta",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/manzana-comercial-x-kg/_/R-00061002-00061002-200?Dy=1",
                }
    },                     
        "manzana_roja_elegida": {
        "nombre": "Manzana Elegida",        
        "unidad": "kg",        
        "categoria": "Fruta",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/manzana-red-elegida-x-kg/_/R-00000528-00000528-200?Dy=1",
                }
    },                       
        "manzana_verde": {
        "nombre": "Manzana Verde",        
        "unidad": "kg",        
        "categoria": "Fruta",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/manzana-g-smith-xkg/_/R-00000527-00000527-200?Dy=1",
                }
    },                             
        "mandarina_criolla": {
        "nombre": "Mandarina Criolla",        
        "unidad": "kg",        
        "categoria": "Fruta",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/mandarina-criolla-xkg/_/R-00000501-00000501-200?Dy=1",
                }
    },                           
        "mandarina_nova": {
        "nombre": "Mandarina Nova",        
        "unidad": "kg",        
        "categoria": "Fruta",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/mandarina-nova-x-kg/_/R-00000204-00000204-200?Dy=1",
                }
    },                      
        "limon": {
        "nombre": "Limon",        
        "unidad": "kg",        
        "categoria": "Fruta",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/limon-comercia-xkg/_/R-00061007-00061007-200?Dy=1",
                }
    },                         
        "kiwi": {
        "nombre": "Kiwi",        
        "unidad": "kg",        
        "categoria": "Fruta",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/kiwi-selecci%C3%B3n-x-kg/_/R-00000496-00000496-200?Dy=1",
                }
    },                             
        "arandanos_solimeno": {
        "nombre": "Arandanos Solimeno",        
        "unidad": "gr",        
        "categoria": "Fruta",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/frutas-congeladas-ar%C3%A1ndanos-solimeno-500g/_/R-00566036-00566036-200?Dy=1&assemblerContentCollection=%2Fcontent%2FShared%2FAuto-Suggest%20Panels",
                }
    },                                
        "arandanos_karinat": {
        "nombre": "Arandanos Karinat",        
        "unidad": "gr",        
        "categoria": "Fruta",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/frutas-arandanos-karinat-doy-300-grm/_/R-00502889-00502889-200?Dy=1&assemblerContentCollection=%2Fcontent%2FShared%2FAuto-Suggest%20Panels",
                }
    },                                
        "arandanos_quillen": {
        "nombre": "Arandanos Quillen",        
        "unidad": "gr",        
        "categoria": "Fruta",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/frutas-congeladas-ar%C3%A1ndanos-quillen-400g/_/R-00604305-00604305-200?Dy=1&assemblerContentCollection=%2Fcontent%2FShared%2FAuto-Suggest%20Panels",
                }
    },                                
        "nuez_cascara": {
        "nombre": "Nuez con Cascara",        
        "unidad": "kg",        
        "categoria": "Fruta",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/nuez-grande-c-cascar-xkg/_/R-00017749-00017749-200?Dy=1",
                }
    },                                   
        "yogurt_ilolay_vainilla": {
        "nombre": "Yogurt Ilolay Vainilla",        
        "unidad": "gr",        
        "categoria": "Lacteo",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/yogur-entero-ilolay-vainilla-bebible-900g/_/R-00013922-00013922-200",
                }
    },                                      
        "yogurt_ilolay_vainilla_descremado": {
        "nombre": "Yogurt Ilolay Vainilla Descremado",        
        "unidad": "gr",        
        "categoria": "Lacteo",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/yogur-descremado-ilolay-vainilla-bebible-1kg/_/R-00483171-00483171-200",
                }
    },                                         
        "yogurt_ilolay_frutilla_descremado": {
        "nombre": "Yogurt Ilolay Frutilla Descremado",        
        "unidad": "gr",        
        "categoria": "Lacteo",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/yogur-descremado-ilolay-frutilla-bebible-1kg/_/R-00483170-00483170-200",
                }
    },                                           
        "yogurt_ilolay_durazno": {
        "nombre": "Yogurt Ilolay Durazno",        
        "unidad": "gr",        
        "categoria": "Lacteo",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/yogur-ilolay-durazno-bebible-1kg/_/R-00483169-00483169-200",
                }
    },                                      
        "yogurt_ilolay_frutilla_kiwi": {
        "nombre": "Yogurt Ilolay Frutilla kiwi",        
        "unidad": "gr",        
        "categoria": "Lacteo",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/yogur-bebible-parcialmente-descremado-frutilla-kiwi-ilolay-900-gr/_/R-00546792-00546792-200",
                }
    },                                      
        "yogurt_milkaut_descremado": {
        "nombre": "Yogurt Milkaut Vainilla Descremado",        
        "unidad": "gr",        
        "categoria": "Lacteo",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/yogur-bebible-descremado-sabor-vainilla-milkaut-900g/_/R-00562336-00562336-200?Dy=1",
                }
    },                                         
        "yogurt_milkaut_vainilla_descremado": {
        "nombre": "Yogurt Milkaut Vainilla Descremado",        
        "unidad": "gr",        
        "categoria": "Lacteo",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/yogur-bebible-entero-fortificado-vainilla-milkaut-1-2-kg/_/R-00511818-00511818-200?Dy=1",
                }
    },                                         
        "yogurt_milkaut_frutilla_descremado": {
        "nombre": "Yogurt Milkaut Frutilla Descremado",        
        "unidad": "gr",        
        "categoria": "Lacteo",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/yogur-bebible-entero-fortificado-vainilla-milkaut-1-2-kg/_/R-00511818-00511818-200?Dy=1",
                }
    },                                            
        "yogurt_milkaut_lactosa": {
        "nombre": "Yogurt Milkaut Vainilla 0 Lactosa",        
        "unidad": "gr",        
        "categoria": "Lacteo",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/yogur-bebible-descremado-sabor-frutilla-milkaut-900g/_/R-00562324-00562324-200?Dy=1",
                }
    },                                            
        "yogurt_milkaut_durazno": {
        "nombre": "Yogurt Milkaut Durazno",        
        "unidad": "gr",        
        "categoria": "Lacteo",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/yogur-bebible-entero-durazno-milkaut-sch-900-grm/_/R-00521116-00521116-200?Dy=1",
                }
    },                                            
        "yogurt_milkaut_vainilla": {
        "nombre": "Yogurt Milkaut Vainilla",        
        "unidad": "gr",        
        "categoria": "Lacteo",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/yogur-bebible-entero-vainilla-milkaut-sch-900-grm/_/R-00521115-00521115-200?Dy=1",
                }
    },                                            
        "yogurt_milkaut_frutilla_fortificado": {
        "nombre": "Yogurt Milkaut Frutilla Fortificado",        
        "unidad": "gr",        
        "categoria": "Lacteo",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/yog-beb-ent-fort-fru-milkaut-sch-1250-kgm/_/R-00510422-00510422-200?Dy=1",
                }
    },                                            
        "casancrem_grande": {
        "nombre": "Casancrem 500 gr",        
        "unidad": "gr",        
        "categoria": "Lacteo",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/queso-crema-cl%C3%A1sico-casancrem-500gr/_/R-00592566-00592566-200?Dy=1",
                "Dia": "https://diaonline.supermercadosdia.com.ar/queso-crema-clasico-casancrem-500-gr-2797/p"
                }
    },                                            
        "casancrem_chico": {
        "nombre": "Casancrem 290 gr",        
        "unidad": "gr",        
        "categoria": "Lacteo",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/queso-crema-cl%C3%A1sico-casancrem-290gr/_/R-00572016-00572016-200?Dy=1",
                }
    },                                            
        "manteca_chica_serenisima": {
        "nombre": "Manteca La Serenisima 100 gr",        
        "unidad": "gr",        
        "categoria": "Lacteo",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/manteca-la-serenisima-100gr/_/R-00003817-00003817-200?Dy=1",
                }
    },                                            
        "manteca_grande_serenisima": {
        "nombre": "Manteca La Serenisima 200 gr",        
        "unidad": "gr",        
        "categoria": "Lacteo",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/manteca-la-serenisima-200gr/_/R-00003818-00003818-200?Dy=1",
                }
    },                                            
        "queso_rallado_serenisima_130": {
        "nombre": "Queso Rallado La Serenisima 130 gr",        
        "unidad": "gr",        
        "categoria": "Lacteo",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/queso-rallado-reggianito-la-serenisima-130g/_/R-00510760-00510760-200?Dy=1",
                }
    },                                            
        "queso_rallado_serenisima_175": {
        "nombre": "Queso Rallado La Serenisima 175 gr",        
        "unidad": "gr",        
        "categoria": "Lacteo",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/queso-rallado-reggianito-la-serenisima-175g/_/R-00510763-00510763-200?Dy=1",
                }
    },                                            
        "leche_3_ninas": {
        "nombre": "Leche Larga Vida Las tres Ninas",        
        "unidad": "gr",        
        "categoria": "Lacteo",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/leche-larga-vida-entera-las-tres-ni%C3%B1as-ttb-1l/_/R-00254550-00254550-200",
                }
    },                                            
        "leche_serenisima": {
        "nombre": "Leche Larga Vida La Serenisima",        
        "unidad": "gr",        
        "categoria": "Lacteo",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/leche-larga-vida-entera-ua-clasica-3-la-serenisima-1l/_/R-00251875-00251875-200",
                }
    },                                            
        "bizcochuelo_morixe": {
        "nombre": "Bizcochuelo Morixe Chocolate",        
        "unidad": "gr",        
        "categoria": "Almacen",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/bizcochuelo-sabor-chocolate-morixe-540-grm/_/R-00541561-00541561-200?Dy=1",
                }
    },                                            
        "arroz_molinos_ala_grande": {
        "nombre": "Arroz Molinos Ala 1 Kg",        
        "unidad": "kg",        
        "categoria": "Almacen",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/arroz-largo-fino-molinos-ala-paquete-1-kg/_/R-00002270-00002270-200?Dy=1",
                }
    },                                            
        "arroz_molinos_ala_chico": {
        "nombre": "Arroz Molinos Ala 500 gr",        
        "unidad": "gr",        
        "categoria": "Almacen",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/arroz-largo-fino-molinos-ala-paquete-1-kg/_/R-00002270-00002270-200?Dy=1",
                }
    },                                            
        "harina_pizza_morixe": {
        "nombre": "Harina 0000 Morixe",        
        "unidad": "gr",        
        "categoria": "Almacen",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/harina-trigo-0000-morixe-1kg/_/R-00480052-00480052-200?Dy=1",
                }
    },                                            
        "harina_pizza_favorita": {
        "nombre": "Harina 0000 Favorita",        
        "unidad": "kg",        
        "categoria": "Almacen",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/harina-trigo-0000-fortificado-con-hierro-favorita-1kg/_/R-00577876-00577876-200?Dy=1",
                }
    },                                            
        "harina_pizza_blancaflor": {
        "nombre": "Harina 0000 Blancaflor",        
        "unidad": "kg",        
        "categoria": "Almacen",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/harina-trigo-0000-blancaflor-1kg/_/R-00581616-00581616-200?Dy=1",
                }
    },                                            
        "harina_pizza_pureza": {
        "nombre": "Harina 0000 Pureza",        
        "unidad": "kg",        
        "categoria": "Almacen",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/harina-de-trigo-pureza-0000-paquete-1-kg/_/R-00253696-00253696-200?Dy=1",
                }
    },                                            
        "tomate_lata_campanola": {
        "nombre": "Tomate Perita La Campanola Lata",        
        "unidad": "unidad",        
        "categoria": "Almacen",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/tomate-perita-la-campagnola-lata-400-gr/_/R-00046126-00046126-200?Dy=1",
                }
    },                                            
        "lentejas_coto": {
        "nombre": "Lentejas Coto",        
        "unidad": "unidad",        
        "categoria": "Almacen",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/lentejas-coto-bolsa-400-gr/_/R-00171605-00171605-200?Dy=1",
                }
    },                                            
        "lentejas_elio": {
        "nombre": "Lentejas Don Elio",        
        "unidad": "unidad",        
        "categoria": "Almacen",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/lentejas-elio-bolsa-400-gr/_/R-00027685-00027685-200?Dy=1",
                }
    },                                            
        "polenta_morixe": {
        "nombre": "Polenta Morixe",        
        "unidad": "kg",        
        "categoria": "Almacen",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/polenta-morixe-1kg/_/R-00511516-00511516-200?Dy=1",
                }
    },                                            
        "polenta_presto": {
        "nombre": "Polenta Presto Pronta",        
        "unidad": "gr",        
        "categoria": "Almacen",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/polenta-instantanea-presto-pronta-paq-730-grm/_/R-00532414-00532414-200?Dy=1",
                 }
    },                                            
        "higienico_higienol": {
        "nombre": "Papel Higiénico HIGIENOL Plus Doble Hoja 20 M 4 Un",        
        "unidad": "4 Unidades x 20 mts",        
        "categoria": "Limpieza",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/papel-higi%C3%A9nico-higienol-plus-doble-hoja-20-m-4-un/_/R-00588926-00588926-200?Dy=1",
                 }
    },                                            
        "higienico_higienol2": {
        "nombre": "Papel Higiénico HIGIENOL Plus Fusión Doble Hoja 30 M 4 Un",        
        "unidad": "4 Unidades x 30 mts",        
        "categoria": "Limpieza",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/papel-higi%C3%A9nico-higienol-plus-fusi%C3%B3n-doble-hoja-30-m-4-un/_/R-00580544-00580544-200?Dy=1",
                "Dia": "https://diaonline.supermercadosdia.com.ar/papel-higienico-higienol-plus-fusion-doble-hoja-30-m-4-ud-301701/p",
                "Jumbo": "https://www.jumbo.com.ar/papel-higienico-plus-fusion-doble-hoja-30-m-x-4-un-higienol/p",
                "Carrefour": "https://www.carrefour.com.ar/papel-higienico-doble-hoja-higienol-plus-x4-30-mts-736162/p"
                 }
    },                                           
        "higienol_gigante": {
        "nombre": "Papel higiénico doble hoja Higienol Plus 30 mts 18 uni",        
        "unidad": "18 Unidades x 30 mts",        
        "categoria": "Limpieza",
        "urls": {                
                "Carrefour": "https://www.carrefour.com.ar/papel-higienico-doble-hoja-higienol-plus-30-mts-18-uni-761669/p"
                 }
    },                                                   
        "higienol_premium": {
        "nombre": "Papel Higiénico Higienol Balance Doble Hoja 30 M 4 Ud.",        
        "unidad": "4 Unidades x 30 mts",        
        "categoria": "Limpieza",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/papel-higi%C3%A9nico-higienol-premium-doble-hoja-30-m-4-un/_/R-00580867-00580867-200?Dy=1",
                "Dia": "https://diaonline.supermercadosdia.com.ar/papel-higienico-higienol-balance-doble-hoja-30-m-4-ud-180072/p",
                "Jumbo": "https://www.jumbo.com.ar/papel-higienico-premium-doble-hoja-30-m-x-4-un-higienol/p",
                "Carrefour": "https://www.carrefour.com.ar/papel-higienico-higienol-premium-doble-hoja-30-mts-4-uni-736165/p"
                 }
    },                                           
        "higienico_felpita": {
        "nombre": "Papel Higiénico FELPITA Doble Hoja Paquete 4 Unidades",        
        "unidad": "4 Unidades x 30 mts",        
        "categoria": "Limpieza",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/papel-higi%C3%A9nico-felpita-doble-hoja-paquete-4-unidades/_/R-00467248-00467248-200?Dy=1",
                 "Carrefour": "https://www.carrefour.com.ar/papel-higienico-doble-hoja-felpita-infinity-4-u-x-30-m/p"
                 }
    },                                            
        "higienico_jumbo": {
        "nombre": "Papel Higienico Doble Hoja 4x30 M Family Care Mp",        
        "unidad": "4 Unidades x 30 mts",        
        "categoria": "Limpieza",
        "urls": {
                "Jumbo":"https://www.jumbo.com.ar/papel-higienico-doble-hoja-4x30-m-family-care-mp-2/p"
                 }
    },                                            
        "higienico_dia": {
        "nombre": "Papel Higiénico Doble Hoja 30 mts 4 Ud.",        
        "unidad": "4 Unidades x 30 mts",        
        "categoria": "Limpieza",
        "urls": {
                "Dia":"https://diaonline.supermercadosdia.com.ar/papel-higienico-doble-hoja-30-mts-4-ud-16949/p"
                 }
    },                                            
        "higienico_dia_grande": {
        "nombre": "Papel Higiénico Doble Hoja 30mts 6 Ud",        
        "unidad": "6 Unidades x 30 mts",        
        "categoria": "Limpieza",
        "urls": {
                "Dia":"https://diaonline.supermercadosdia.com.ar/papel-higienico-doble-hoja-30mts-6-ud-834/p"
                 }
    },                                            
        "higienico_carrefour": {
        "nombre": "Papel higiénico doble hoja Carrefour Essential 4 x 30 mts",        
        "unidad": "6 Unidades x 30 mts",        
        "categoria": "Limpieza",
        "urls": {
                "Carrefour":"https://www.carrefour.com.ar/papel-higienico-doble-hoja-carrefour-essential-4-x-30-mts-597038/p"
                 }
    },                                            
        "higienico_carrefour_decorado": {
        "nombre": "Papel higiénico doble hoja deco Carrefour Essential 50 mts. x 4 uni",        
        "unidad": "6 Unidades x 50 mts",        
        "categoria": "Limpieza",
        "urls": {
                "Carrefour":"https://www.carrefour.com.ar/papel-higienico-doble-hoja-deco-carrefour-essential-50-mts-x-4-uni/p"
                 }
    },                                            
        "higienico_noble": {
        "nombre": "Papel higiénico Noble doble hoja 30 mts 4 uni",        
        "unidad": "4 Unidades x 30 mts",        
        "categoria": "Limpieza",
        "urls": {
                "Carrefour":"https://www.carrefour.com.ar/papel-higienico-noble-doble-hoja-30-mts-4-uni-751386/p"
                 }
    },                                            
        "higienico_elegante": {
        "nombre": "Papel higiénico doble hoja Elegante 4 x 30 m.",        
        "unidad": "4 Unidades x 30 mts",        
        "categoria": "Limpieza",
        "urls": {
                "Carrefour":"https://www.carrefour.com.ar/papel-higienico-doble-hoja-elegante-4-x-30-m-628282/p"
                 }
    },                                            
        "higienico_elegante_rinde": {
        "nombre": "Papel higiénico Elegante hoja doble rindemas 30 mts. x 4 uni",        
        "unidad": "4 Unidades x 30 mts",        
        "categoria": "Limpieza",
        "urls": {
                "Carrefour":"https://www.carrefour.com.ar/papel-higienico-elegante-hoja-doble-rindemas-30-mts-x-4-uni-702838/p"
                 }
    },                                           
        "rollo_cocina_campanita": {
        "nombre": "Rollo Cocina Campanita 100 panios",        
        "unidad": "2",        
        "categoria": "Limpieza",
        "urls": {
                "Coto":"https://www.cotodigital.com.ar/sitios/cdigi/productos/rollo-de-cocina-campanita-100-pa%C3%B1os-paquete-2-unidades/_/R-00272112-00272112-200?Dy=1"
                 }
    },                                           
        "rollo_cocina_sussex": {
        "nombre": "Rollo Cocina Sussex 50 panios",        
        "unidad": "3",        
        "categoria": "Limpieza",
        "urls": {
                "Coto":"https://www.cotodigital.com.ar/sitios/cdigi/productos/rollo-de-cocina-campanita-100-pa%C3%B1os-paquete-2-unidades/_/R-00272112-00272112-200?Dy=1",
                "Jumbo": "https://www.jumbo.com.ar/rollo-cocina-clasico-50-panos-3-un-sussex/p",
                "Dia": "https://diaonline.supermercadosdia.com.ar/rollo-cocina-sussex-clasico-50-panos-3-ud-88515/p"
                 }
    },                                           
        "rollo_cocina_sussex2": {
        "nombre": "Rollo Cocina Sussex 60 panios",        
        "unidad": "3",        
        "categoria": "Limpieza",
        "urls": {
                "Coto":"https://www.cotodigital.com.ar/sitios/cdigi/productos/rollo-de-cocina-sussex-ultra-60-pa%C3%B1os-3-un/_/R-00580697-00580697-200?Dy=1",
                
                 }
    },                                         
        "rollo_cocina_sussex3": {
        "nombre": "Rollo Cocina Sussex 100 panios",        
        "unidad": "3",        
        "categoria": "Limpieza",
        "urls": {
                "Jumbo":"https://www.jumbo.com.ar/rollo-de-cocina-ultra-100-panos-3-un-sussex/p",
                
                 }
    },




}