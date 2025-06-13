from datetime import datetime
import pandas as pd

FECHA = datetime.now().strftime("%Y-%m-%d")

URLS_DEBUG = {
    "bife_americano": {
        "nombre": "Bife Americano",        
        "unidad": "KG",        
        "categoria": "Carnes",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/bife-americano-x-kg/_/R-00041414-00041414-200?Dy=1",
                }
    }
}


URLS = {
    "bife_americano": {
        "nombre": "Bife Americano",        
        "unidad": "KG",        
        "categoria": "Carnes",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/bife-americano-x-kg/_/R-00041414-00041414-200?Dy=1",
                }
    },
    "ojo_bife": {
        "nombre": "Ojo de Bife",        
        "unidad": "KG",        
        "categoria": "Carnes",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/ojo-de-bife-coto-xkg/_/R-00029810-00029810-200?Dy=1",
                }
    },
    "bife_chorizo": {
        "nombre": "Bife de Chorizo",        
        "unidad": "KG",        
        "categoria": "Carnes",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/bife-de-chorizo-coto-xkg/_/R-00029804-00029804-200?Dy=1",
                }
    },    
    "cuadril": {
        "nombre": "Cuadril",        
        "unidad": "KG",        
        "categoria": "Carnes",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/cuadril-selecci%C3%B3n-x-kg/_/R-00042317-00042317-200?Dy=1",
                }
    },
        "picada_desgrasada": {
        "nombre": "Picada Desgrasada",        
        "unidad": "KG",        
        "categoria": "Carnes",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/picada-desgrasada-estancias-coto-x-kg/_/R-00048124-00048124-200?Dy=1",
                }
    },
        "bola_lomo": {
        "nombre": "Bola de Lomo",        
        "unidad": "KG",        
        "categoria": "Carnes",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/bola-de-lomo-estancias-coto-x-kg/_/R-00047993-00047993-200?Dy=1",
                }
    },
        "nalga": {
        "nombre": "Nalga",        
        "unidad": "KG",        
        "categoria": "Carnes",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/nalga-estancias-coto-x-kg/_/R-00047991-00047991-200?Dy=1&assemblerContentCollection=%2Fcontent%2FShared%2FAuto-Suggest%20Panels",
                }
    },
        "peceto": {
        "nombre": "Peceto",        
        "unidad": "KG",        
        "categoria": "Carnes",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/peceto-feteado-x-kg/_/R-00041407-00041407-200?Dy=1",
                }
    },
        "paleta": {
        "nombre": "Paleta",        
        "unidad": "KG",        
        "categoria": "Carnes",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/paleta-del-centro-estancias-coto-x-kg/_/R-00047984-00047984-200?Dy=1",
                }
    },
        "roast_beef": {
        "nombre": "Roast Beef",        
        "unidad": "KG",        
        "categoria": "Carnes",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/roast-beef-estancias-coto-x-kg/_/R-00047985-00047985-200?Dy=1&assemblerContentCollection=%2Fcontent%2FShared%2FAuto-Suggest%20Panels",
                }
    },
    
        "bife_parrilla": {
        "nombre": "Bife de Parrilla",        
        "unidad": "KG",        
        "categoria": "Carnes",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/bife-parrilla-estancias-coto-x-kg/_/R-00048129-00048129-200?Dy=1",
                }
    },    
        "pollo": {
        "nombre": "Pollo Entero",        
        "unidad": "KG",        
        "categoria": "Carnes",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/pollo-congelado-x-kg/_/R-00042989-00042989-200?Dy=1",
                }
    },
    "carre_cerdo": {
        "nombre": "Carre de Cerdo",        
        "unidad": "KG",        
        "categoria": "Carnes",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/carr%C3%A9-de-cerdo-x-kg/_/R-00017162-00017162-200?Dy=1",
                }
    },    
    "bondiola_cerdo": {
        "nombre": "Bondiola de Cerdo",        
        "unidad": "KG",        
        "categoria": "Carnes",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/bondiola-de-cerdo-x-kg/_/R-00000943-00000943-200?Dy=1&assemblerContentCollection=%2Fcontent%2FShared%2FAuto-Suggest%20Panels",
                }
    },     
        "papa_negra": {
        "nombre": "Papa Negra",        
        "unidad": "KG",        
        "categoria": "Verdura",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/papa-negra-selecci%C3%B3n-x-kg/_/R-00060947-00060947-200?Dy=1",
                }
    },    
        "cebolla": {
        "nombre": "Cebolla",        
        "unidad": "KG",        
        "categoria": "Verdura",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/cebolla-a-granel-x-kg/_/R-00000602-00000602-200?Dy=1",
                }
    },    
        "coliflor": {
        "nombre": "Coliflor",        
        "unidad": "KG",        
        "categoria": "Verdura",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/coliflor-x-kg/_/R-00000619-00000619-200?Dy=1",
                }
    },    
        "repollo_colorado": {
        "nombre": "Repollo Colorado",        
        "unidad": "KG",        
        "categoria": "Verdura",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/repollo-colorado-x-kg/_/R-00000680-00000680-200?Dy=1",
                }
    }, 
        "repollo_blanco": {
        "nombre": "Repollo Blanco",        
        "unidad": "KG",        
        "categoria": "Verdura",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/repollo-blanco-x-kg/_/R-00000678-00000678-200?Dy=1",
                }
    },    
        "zanahoria": {
        "nombre": "Zanahoria",        
        "unidad": "KG",        
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
        "unidad": "KG",        
        "categoria": "Verdura",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/lechuga-mantecosa-x-kg/_/R-00000424-00000424-200?Dy=1",
                }
    }, 

        "lechuga_capuchina": {
        "nombre": "Lechuga Capuchina",        
        "unidad": "KG",        
        "categoria": "Verdura",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/lechuga-capuchina-x-kg/_/R-00000648-00000648-200?Dy=1",
                }   
    },             
        "lechuga_criolla": {
        "nombre": "Lechuga Criolla",        
        "unidad": "KG",        
        "categoria": "Verdura",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/lechuga-criolla-x-kg/_/R-00000649-00000649-200?Dy=1",
                }
    },             
        "lechuga_francesa": {
        "nombre": "Lechuga Francesa",        
        "unidad": "KG",        
        "categoria": "Verdura",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/lechuga-francesa-x-kg/_/R-00000650-00000650-200?Dy=1",
                }
    },             
        "brocoli": {
        "nombre": "Brocoli",        
        "unidad": "KG",        
        "categoria": "Verdura",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/brocoli-x-kg/_/R-00000598-00000598-200",
                }
    },             
        "jengibre": {
        "nombre": "Jengibre",        
        "unidad": "KG",        
        "categoria": "Verdura",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/jengibre-x-kg/_/R-00092926-00092926-200",
                }
    },             
        "pimiento_rojo": {
        "nombre": "Pimiento Rojo",        
        "unidad": "KG",        
        "categoria": "Verdura",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/pimiento-rojo-xkg/_/R-00000671-00000671-200?Dy=1",
                }
    },             
        "zapallo_anco": {
        "nombre": "Zapallo Anco",        
        "unidad": "KG",        
        "categoria": "Verdura",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/zapallo-anco-x-kg/_/R-00000688-00000688-200?Dy=1",
                }
    },             
        "remolacha": {
        "nombre": "Remolacha",        
        "unidad": "KG",        
        "categoria": "Verdura",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/remolacha-x-kg/_/R-00000677-00000677-200",
                }
    },             
        "tomate_redondo": {
        "nombre": "Tomate Redondo",        
        "unidad": "KG",        
        "categoria": "Verdura",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/tomate-red-x-kg/_/R-00000684-00000684-200?Dy=1&assemblerContentCollection=%2Fcontent%2FShared%2FAuto-Suggest%20Panels",
                }
    },             
        "tomate_perita": {
        "nombre": "Tomate Perita",        
        "unidad": "KG",        
        "categoria": "Verdura",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/tomate-perit-xkg/_/R-00000683-00000683-200?Dy=1&assemblerContentCollection=%2Fcontent%2FShared%2FAuto-Suggest%20Panels",
                }
    },             
        "banana": {
        "nombre": "Banana",        
        "unidad": "KG",        
        "categoria": "Fruta",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/banana-cavendish-x-kg/_/R-00000446-00000446-200?Dy=1",
                }
    },             
        "naranja_jugo": {
        "nombre": "Naranja Jugo",        
        "unidad": "KG",        
        "categoria": "Fruta",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/naranja-jugo-xkg/_/R-00061005-00061005-200?Dy=1&assemblerContentCollection=%2Fcontent%2FShared%2FAuto-Suggest%20Panels",
                }
    },                 
        "uva_red_glove": {
        "nombre": "Uva Red Glove",        
        "unidad": "KG",        
        "categoria": "Fruta",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/uva-red-globe-xkg/_/R-00000861-00000861-200?Dy=1&assemblerContentCollection=%2Fcontent%2FShared%2FAuto-Suggest%20Panels",
                }
    },                     
        "manzana_roja": {
        "nombre": "Manzana Roja",        
        "unidad": "KG",        
        "categoria": "Fruta",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/manzana-comercial-x-kg/_/R-00061002-00061002-200?Dy=1",
                }
    },                     
        "manzana_roja_elegida": {
        "nombre": "Manzana Elegida",        
        "unidad": "KG",        
        "categoria": "Fruta",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/manzana-red-elegida-x-kg/_/R-00000528-00000528-200?Dy=1",
                }
    },                       
        "manzana_verde": {
        "nombre": "Manzana Verde",        
        "unidad": "KG",        
        "categoria": "Fruta",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/manzana-g-smith-xkg/_/R-00000527-00000527-200?Dy=1",
                }
    },                             
        "mandarina_criolla": {
        "nombre": "Mandarina Criolla",        
        "unidad": "KG",        
        "categoria": "Fruta",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/mandarina-criolla-xkg/_/R-00000501-00000501-200?Dy=1",
                }
    },                           
        "mandarina_nova": {
        "nombre": "Mandarina Nova",        
        "unidad": "KG",        
        "categoria": "Fruta",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/mandarina-nova-x-kg/_/R-00000204-00000204-200?Dy=1",
                }
    },                      
        "limon": {
        "nombre": "Limon",        
        "unidad": "KG",        
        "categoria": "Fruta",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/limon-comercia-xkg/_/R-00061007-00061007-200?Dy=1",
                }
    },                         
        "kiwi": {
        "nombre": "Kiwi",        
        "unidad": "KG",        
        "categoria": "Fruta",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/kiwi-selecci%C3%B3n-x-kg/_/R-00000496-00000496-200?Dy=1",
                }
    },                             
        "arandanos_solimeno": {
        "nombre": "Arandanos Solimeno",        
        "unidad": "GR",        
        "categoria": "Fruta",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/frutas-congeladas-ar%C3%A1ndanos-solimeno-500g/_/R-00566036-00566036-200?Dy=1&assemblerContentCollection=%2Fcontent%2FShared%2FAuto-Suggest%20Panels",
                }
    },                                
        "arandanos_karinat": {
        "nombre": "Arandanos Karinat",        
        "unidad": "GR",        
        "categoria": "Fruta",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/frutas-arandanos-karinat-doy-300-grm/_/R-00502889-00502889-200?Dy=1&assemblerContentCollection=%2Fcontent%2FShared%2FAuto-Suggest%20Panels",
                }
    },                                
        "arandanos_quillen": {
        "nombre": "Arandanos Quillen",        
        "unidad": "GR",        
        "categoria": "Fruta",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/frutas-congeladas-ar%C3%A1ndanos-quillen-400g/_/R-00604305-00604305-200?Dy=1&assemblerContentCollection=%2Fcontent%2FShared%2FAuto-Suggest%20Panels",
                }
    },                 
                



    }

    
    
    
    
