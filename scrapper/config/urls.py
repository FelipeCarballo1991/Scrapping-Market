from datetime import datetime
import pandas as pd

FECHA = datetime.now().strftime("%d-%m-%Y")
FECHA_COMPLETA = datetime.now().strftime("%Y-%m-%d_%H:%M_%S")


URLS_DEBUG = {
     "naranja_jugo": {
        "nombre": "Naranja Jugo",        
        "unidad": "1",        
        "categoria": "Fruta",
        "urls": {
                "Carrefour": "https://www.carrefour.com.ar/naranja-de-jugo-x-kg-8314/p",
                # "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/ojo-de-bife-coto-xkg/_/R-00029810-00029810-200?Dy=1",
                # "Jumbo":"https://www.jumbo.com.ar/rollo-de-cocina-ultra-100-panos-3-un-sussex/p",
                # "Dia":"https://diaonline.supermercadosdia.com.ar/queso-crema-clasico-casancrem-500-gr-2797/p",

                }
        },"bife_americano": {
        "nombre": "Bife Americano",        
        "unidad": "1",        
        "categoria": "Carnes",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/bife-americano-x-kg/_/R-00041414-00041414-200?Dy=1",
                # "Dia": "",
                "Jumbo": "https://www.jumbo.com.ar/paleta-americano-la-hacienda/p",
                "Carrefour": "https://www.carrefour.com.ar/bife-americano-novillito-x-kg-678556/p"
                
                }
        },                                            
        "casancrem_grande": {
        "nombre": "Casancrem 500 gr",        
        "unidad": "0.5",        
        "categoria": "Lacteo",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/queso-crema-cl%C3%A1sico-casancrem-500gr/_/R-00592566-00592566-200?Dy=1",
                "Dia": "https://diaonline.supermercadosdia.com.ar/queso-crema-clasico-casancrem-500-gr-2797/p",
                "Jumbo": "https://www.jumbo.com.ar/queso-crema-clasico-500-gr-casancrem/p",
                "Carrefour": "https://www.carrefour.com.ar/queso-crema-casancrem-clasico-500-grs-748003/p"
                }
    }
        

}

URLS = {
    "bife_americano": {
        "nombre": "Bife Americano",        
        "unidad": "1",        
        "categoria": "Carnes",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/bife-americano-x-kg/_/R-00041414-00041414-200?Dy=1",
                # "Dia": "",
                "Jumbo": "https://www.jumbo.com.ar/paleta-americano-la-hacienda/p",
                "Carrefour": "https://www.carrefour.com.ar/bife-americano-novillito-x-kg-678556/p"
                
                }
    },
    "ojo_bife": {
        "nombre": "Ojo de Bife",        
        "unidad": "1",        
        "categoria": "Carnes",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/ojo-de-bife-coto-xkg/_/R-00029810-00029810-200?Dy=1",
                # "Dia": "",
                # "Jumbo": "",
                "Carrefour": "https://www.carrefour.com.ar/ojo-de-bife-novillito-x-kg-57289/p"
                
                }
    },
    "bife_chorizo": {
        "nombre": "Bife de Chorizo",        
        "unidad": "1",        
        "categoria": "Carnes",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/bife-de-chorizo-coto-xkg/_/R-00029804-00029804-200?Dy=1",
                # "Dia": "",
                "Jumbo": "https://www.jumbo.com.ar/bife-de-chorizo-4/p",
                "Carrefour": "https://www.carrefour.com.ar/bife-de-chorizo-novillito-x-kg-662854/p"
                }
    },    
    "cuadril": {
        "nombre": "Cuadril",        
        "unidad": "1",        
        "categoria": "Carnes",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/cuadril-selecci%C3%B3n-x-kg/_/R-00042317-00042317-200?Dy=1",
                # "Dia": "",
                # "Jumbo": "",
                "Carrefour": "https://www.carrefour.com.ar/cuadril-novillito-x-kg-662857/p"
                }
    },
        "picada_desgrasada": {
        "nombre": "Picada Desgrasada",        
        "unidad": "1",        
        "categoria": "Carnes",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/picada-desgrasada-estancias-coto-x-kg/_/R-00048124-00048124-200?Dy=1",
                # "Dia": "",
                # "Jumbo": "",
                "Carrefour": "https://www.carrefour.com.ar/picada-tartare-etiqueta-negra-x-kg-678598/p"         
                
                }
    },
        "bola_lomo": {
        "nombre": "Bola de Lomo",        
        "unidad": "1",        
        "categoria": "Carnes",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/bola-de-lomo-estancias-coto-x-kg/_/R-00047993-00047993-200?Dy=1",
                # "Dia": "",
                "Jumbo": "https://www.jumbo.com.ar/milanesa-bola-de-lomo-la-hacienda/p",
                "Carrefour": "https://www.carrefour.com.ar/milanesa-de-bola-de-lomo-novillito-x-kg-662861/p"
                }
    },
        "nalga": {
        "nombre": "Nalga",        
        "unidad": "1",        
        "categoria": "Carnes",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/nalga-estancias-coto-x-kg/_/R-00047991-00047991-200?Dy=1&assemblerContentCollection=%2Fcontent%2FShared%2FAuto-Suggest%20Panels",
                # "Dia": "",
                # "Jumbo": "",
                "Carrefour": "https://www.carrefour.com.ar/milanesa-de-nalga-novillito-x-kg-722862/p" 
                }
    },
        "peceto": {
        "nombre": "Peceto",        
        "unidad": "1",        
        "categoria": "Carnes",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/peceto-feteado-x-kg/_/R-00041407-00041407-200?Dy=1",
                # "Dia": "",
                # "Jumbo": "",
                "Carrefour": "https://www.carrefour.com.ar/peceto-feteado-novillito-x-kg-678567/p" 
                }
    },
        "paleta": {
        "nombre": "Paleta",        
        "unidad": "1",        
        "categoria": "Carnes",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/paleta-del-centro-estancias-coto-x-kg/_/R-00047984-00047984-200?Dy=1",
                # "Dia": "",
                "Jumbo": "https://www.jumbo.com.ar/milanesa-bola-de-lomo-la-hacienda/p",
                "Carrefour": "https://www.carrefour.com.ar/paleta-novillito-x-kg-662865/p"
                
                }
    },
        "roast_beef": {
        "nombre": "Roast Beef",        
        "unidad": "1",        
        "categoria": "Carnes",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/roast-beef-estancias-coto-x-kg/_/R-00047985-00047985-200?Dy=1&assemblerContentCollection=%2Fcontent%2FShared%2FAuto-Suggest%20Panels",
                # "Dia": "",
                "Jumbo": "https://www.jumbo.com.ar/roast-beef-churrasco/p",
                "Carrefour": "https://www.carrefour.com.ar/roast-beef-novillito-x-kg-662867/p"
                
                }
    },
    
        "bife_parrilla": {
        "nombre": "Bife de Parrilla",        
        "unidad": "1",        
        "categoria": "Carnes",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/bife-parrilla-estancias-coto-x-kg/_/R-00048129-00048129-200?Dy=1",
                # "Dia": "",
                # "Jumbo": "",
                # "Carrefour": ""
                
                }
    },    
        "pollo": {
        "nombre": "Pollo Entero",        
        "unidad": "1",        
        "categoria": "Carnes",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/pollo-congelado-x-kg/_/R-00042989-00042989-200?Dy=1",
                # "Dia": "",
                "Jumbo": "https://www.jumbo.com.ar/pollo-fresco-con-menudos-2/p",
                # "Carrefour": "https://www.carrefour.com.ar/pollo-entero-congelado-x-kg-699692/p"
                
                }
    },
        
        "pechuga": {
        "nombre": "Pechuga",        
        "unidad": "1",        
        "categoria": "Carnes",
        "urls": {
                # "Coto": "",
                # "Dia": "",
                "Jumbo": "https://www.jumbo.com.ar/suprema-de-pollo-granel-fresca/p",
                # "Carrefour": ""
                
                }
    },    
        
        "pata_muslo": {
        "nombre": "Pata Muslo",        
        "unidad": "1",        
        "categoria": "Carnes",
        "urls": {
                # "Coto": "",
                # "Dia": "",
                "Jumbo": "https://www.jumbo.com.ar/cuarto-trasero-de-pollo-granel-fresco/p",
                # "Carrefour": ""
                
                }
    },
    "carre_cerdo": {
        "nombre": "Carre de Cerdo",        
        "unidad": "1",        
        "categoria": "Carnes",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/carr%C3%A9-de-cerdo-x-kg/_/R-00017162-00017162-200?Dy=1",
                # "Dia": "",
                "Jumbo": "https://www.jumbo.com.ar/carre-de-cerdo-con-hueso-fresco-2/p",
                "Carrefour": "https://www.carrefour.com.ar/carre-de-cerdo-con-hueso-x-kg-687687/p"
                
                }
    },    
    "bondiola_cerdo": {
        "nombre": "Bondiola de Cerdo",        
        "unidad": "1",        
        "categoria": "Carnes",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/bondiola-de-cerdo-x-kg/_/R-00000943-00000943-200?Dy=1&assemblerContentCollection=%2Fcontent%2FShared%2FAuto-Suggest%20Panels",
                # "Dia": "",
                "Jumbo": "https://www.jumbo.com.ar/bondiola-de-cerdo-fresca-x-kg-2-2/p",
                "Carrefour": "https://www.carrefour.com.ar/bondiola-de-cerdo-x-kg--687691/p"
                
                }
    },     
        "papa_negra": {
        "nombre": "Papa Negra",        
        "unidad": "1",        
        "categoria": "Verdura",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/papa-negra-selecci%C3%B3n-x-kg/_/R-00060947-00060947-200?Dy=1",
                # "Dia": "",
                "Jumbo": "https://www.jumbo.com.ar/papa-negra-por-kg/p",
                "Carrefour": "https://www.carrefour.com.ar/papa-x-kg-9278/p"
                
                }
    },    
        "cebolla": {
        "nombre": "Cebolla",        
        "unidad": "1",        
        "categoria": "Verdura",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/cebolla-a-granel-x-kg/_/R-00000602-00000602-200?Dy=1",
                # "Dia": "",
                "Jumbo": "https://www.jumbo.com.ar/cebolla-superior-por-kg/p",
                "Carrefour": "https://www.carrefour.com.ar/cebolla-x-kg/p"
                
                }
    },    
        "coliflor": {
        "nombre": "Coliflor",        
        "unidad": "1",        
        "categoria": "Verdura",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/coliflor-x-kg/_/R-00000619-00000619-200?Dy=1",
                # "Dia": "",
                # "Jumbo": "",
                "Carrefour": "https://www.carrefour.com.ar/coliflor-x-kg/p"
                
                }
    },    
        "repollo_colorado": {
        "nombre": "Repollo Colorado",        
        "unidad": "1",        
        "categoria": "Verdura",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/repollo-colorado-x-kg/_/R-00000680-00000680-200?Dy=1",
                # "Dia": "",
                "Jumbo": "https://www.jumbo.com.ar/repollo-colorado-por-kg/p",
                "Carrefour": "https://www.carrefour.com.ar/repollo-colorado-x-kg/p"
                
                }
    }, 
        "repollo_blanco": {
        "nombre": "Repollo Blanco",        
        "unidad": "1",        
        "categoria": "Verdura",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/repollo-blanco-x-kg/_/R-00000678-00000678-200?Dy=1",
                # "Dia": "",
                "Jumbo": "https://www.jumbo.com.ar/repollo-4-2/p",
                "Carrefour": "https://www.carrefour.com.ar/repollo-blanco-x-kg/p"
                
                }
    },    
        "zanahoria": {
        "nombre": "Zanahoria",        
        "unidad": "1",        
        "categoria": "Verdura",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/zanahoria-seleccion-xkg/_/R-00000686-00000686-200?Dy=1",
                # "Dia": "",
                "Jumbo": "https://www.jumbo.com.ar/zanahoria-por-kg/p",
                "Carrefour": "https://www.carrefour.com.ar/zanahoria-x-kg-630573/p"
                
                }
    },
      
        "perejil": {
        "nombre": "Perejil",        
        "unidad": "1",        
        "categoria": "Verdura",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/perejil-x-uni/_/R-00047599-00047599-200?Dy=1",
                # "Dia": "",
                "Jumbo": "https://www.jumbo.com.ar/perejil-por-u/p",
                "Carrefour": "https://www.carrefour.com.ar/perejil-x-1-atado/p"
                
                }
    },             
        "lechuga_mantecosa": {
        "nombre": "Lechuga Mantecosa",        
        "unidad": "1",        
        "categoria": "Verdura",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/lechuga-mantecosa-x-kg/_/R-00000424-00000424-200?Dy=1",
                # "Dia": "",
                "Jumbo": "https://www.jumbo.com.ar/lechuga-mantecosa-por-kg/p",
                "Carrefour": "https://www.carrefour.com.ar/lechuga-mantecosa-x-kg/p"
                
                }
    }, 

        "lechuga_capuchina": {
        "nombre": "Lechuga Capuchina",        
        "unidad": "1",        
        "categoria": "Verdura",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/lechuga-capuchina-x-kg/_/R-00000648-00000648-200?Dy=1",
                # "Dia": "",
                "Jumbo": "https://www.jumbo.com.ar/lechuga-capuchina-por-kg/p",
                "Carrefour": "https://www.carrefour.com.ar/lechuga-capuchina-x-kg/p"
                
                }   
    },             
        "lechuga_criolla": {
        "nombre": "Lechuga Criolla",        
        "unidad": "1",        
        "categoria": "Verdura",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/lechuga-criolla-x-kg/_/R-00000649-00000649-200?Dy=1",
                # "Dia": "",
                # "Jumbo": "",
                "Carrefour": "https://www.carrefour.com.ar/lechuga-criolla-x-kg/p"
                
                }
    },             
        "lechuga_francesa": {
        "nombre": "Lechuga Francesa",        
        "unidad": "1",        
        "categoria": "Verdura",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/lechuga-francesa-x-kg/_/R-00000650-00000650-200?Dy=1",
                # "Dia": "",
                "Jumbo": "https://www.jumbo.com.ar/lechuga-francesa-por-kg/p",
                "Carrefour": "https://www.carrefour.com.ar/lechuga-francesa-x-kg-1/p"
                
                }
    },             
        "brocoli": {
        "nombre": "Brocoli",        
        "unidad": "1",        
        "categoria": "Verdura",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/brocoli-x-kg/_/R-00000598-00000598-200",
                # "Dia": "",
                "Jumbo": "https://www.jumbo.com.ar/brocoli/p",
                "Carrefour": "https://www.carrefour.com.ar/brocoli-x-kg/p"
                
                }
    },             
        "jengibre": {
        "nombre": "Jengibre",        
        "unidad": "1",        
        "categoria": "Verdura",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/jengibre-x-kg/_/R-00092926-00092926-200",
                # "Dia": "",
                "Jumbo": "https://www.jumbo.com.ar/jengibre-por-kg/p",
                "Carrefour": "https://www.carrefour.com.ar/raiz-de-jengibre-x-kg/p"
                
                }
    },             
        "pimiento_rojo": {
        "nombre": "Pimiento Rojo",        
        "unidad": "1",        
        "categoria": "Verdura",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/pimiento-rojo-xkg/_/R-00000671-00000671-200?Dy=1",
                # "Dia": "",
                "Jumbo": "https://www.jumbo.com.ar/pimiento-rojo-superior-2/p",
                "Carrefour": "https://www.carrefour.com.ar/pimiento-rojo-x-kg-2/p"
                
                }
    },             
        "zapallo_anco": {
        "nombre": "Zapallo Anco",        
        "unidad": "1",        
        "categoria": "Verdura",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/zapallo-anco-x-kg/_/R-00000688-00000688-200?Dy=1",
                # "Dia": "",
                "Jumbo": "https://www.jumbo.com.ar/zapallo-coreano-por-kg/p",
                "Carrefour": "https://www.carrefour.com.ar/zapallo-anco-x-kg/p"
                
                }
    },             
        "remolacha": {
        "nombre": "Remolacha",        
        "unidad": "1",        
        "categoria": "Verdura",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/remolacha-x-kg/_/R-00000677-00000677-200",
                # "Dia": "",
                "Jumbo": "https://www.jumbo.com.ar/remolacha-por-kg/p",
                "Carrefour": "https://www.carrefour.com.ar/remolacha-x-kg/p"
                
                }
    },             
        "tomate_redondo": {
        "nombre": "Tomate Redondo",        
        "unidad": "1",        
        "categoria": "Verdura",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/tomate-red-x-kg/_/R-00000684-00000684-200?Dy=1&assemblerContentCollection=%2Fcontent%2FShared%2FAuto-Suggest%20Panels",
                # "Dia": "",
                "Jumbo": "https://www.jumbo.com.ar/tomate-redondo-grande-por-kg/p",
                "Carrefour": "https://www.carrefour.com.ar/tomate-redondo-en-racimo-huella-natural-x-kg/p"
                
                }
    },             
        "tomate_perita": {
        "nombre": "Tomate Perita",        
        "unidad": "1",        
        "categoria": "Verdura",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/tomate-perit-xkg/_/R-00000683-00000683-200?Dy=1&assemblerContentCollection=%2Fcontent%2FShared%2FAuto-Suggest%20Panels",
                # "Dia": "",
                "Jumbo": "https://www.jumbo.com.ar/tomate-perita-por-kg/p",
                "Carrefour": "https://www.carrefour.com.ar/tomate-perita-x-kg/p"
                
                }
    },                 
        "espinaca_granja_sol": {
        "nombre": "Espinaca granja del Sol",        
        "unidad": "1",        
        "categoria": "Verdura",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/espinaca-congelada-granja-del-sol-1kg/_/R-00565167-00565167-200?Dy=1",
                # "Dia": "",
                # "Jumbo": "",
                "Carrefour": "https://www.carrefour.com.ar/espinaca-congelada-granja-del-sol-en-bolsa-1-kg-720850/p"
                
                }
    },                 
        "espinaca_lucchetti": {
        "nombre": "Espinaca Luchetti 400 gr",        
        "unidad": "0.4",        
        "categoria": "Verdura",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/espinaca-congelada-lucchetti-400g/_/R-00565182-00565182-200?Dy=1",
                # "Dia": "",
                "Jumbo": "https://www.jumbo.com.ar/espinaca-lucchetti-400-gr/p",
                "Carrefour": "https://www.carrefour.com.ar/espinaca-lucchetti-en-bolsa-400-g-720853/p"
                
                }
    },               
        "banana": {
        "nombre": "Banana",        
        "unidad": "1",        
        "categoria": "Fruta",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/banana-cavendish-x-kg/_/R-00000446-00000446-200?Dy=1",
                # "Dia": "",
                "Jumbo": "https://www.jumbo.com.ar/banana-ecuador-x-kg/p",
                "Carrefour": "https://www.carrefour.com.ar/banana-seleccion-x-kg-719074/p"
                
                }
    },             
        "naranja_jugo": {
        "nombre": "Naranja Jugo",        
        "unidad": "1",        
        "categoria": "Fruta",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/naranja-jugo-xkg/_/R-00061005-00061005-200?Dy=1&assemblerContentCollection=%2Fcontent%2FShared%2FAuto-Suggest%20Panels",
                # "Dia": "",
                "Jumbo": "https://www.jumbo.com.ar/naranja-para-jugo-por-kg/p",
                "Carrefour": "https://www.carrefour.com.ar/naranja-de-jugo-x-kg-8314/p"
                
                }
    },                 
        "uva_red_glove": {
        "nombre": "Uva Red Glove",        
        "unidad": "1",        
        "categoria": "Fruta",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/uva-red-globe-xkg/_/R-00000861-00000861-200?Dy=1&assemblerContentCollection=%2Fcontent%2FShared%2FAuto-Suggest%20Panels",
                # "Dia": "",
                "Jumbo": "https://www.jumbo.com.ar/uva-red-globe-x-kg/p",
                "Carrefour": "https://www.carrefour.com.ar/uva-rosada-x-kg/p"
                
                }
    },                     
        "manzana_roja": {
        "nombre": "Manzana Roja",        
        "unidad": "1",        
        "categoria": "Fruta",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/manzana-comercial-x-kg/_/R-00061002-00061002-200?Dy=1",
                # "Dia": "",
                "Jumbo": "https://www.jumbo.com.ar/manzana-red-delicius-por-kg/p",
                "Carrefour": "https://www.carrefour.com.ar/manzana-red-x-kg-432782/p"
                
                }
    },                     
        "manzana_roja_elegida": {
        "nombre": "Manzana Elegida",        
        "unidad": "1",        
        "categoria": "Fruta",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/manzana-red-elegida-x-kg/_/R-00000528-00000528-200?Dy=1",
                # "Dia": "",
                "Jumbo": "https://www.jumbo.com.ar/manzana-elegida-por-kg/p",
                "Carrefour": "https://www.carrefour.com.ar/manzana-roja-huella-natural-x-kg/p"
                
                }
    },                       
        "manzana_verde": {
        "nombre": "Manzana Verde",        
        "unidad": "1",        
        "categoria": "Fruta",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/manzana-g-smith-xkg/_/R-00000527-00000527-200?Dy=1",
                # "Dia": "",
                "Jumbo": "https://www.jumbo.com.ar/manzana-gran-smith-x-kg/p",
                "Carrefour": "https://www.carrefour.com.ar/manzana-granny-especial-x-kg-61585/p"
                
                }
    },                             
        "mandarina_criolla": {
        "nombre": "Mandarina Criolla",        
        "unidad": "1",        
        "categoria": "Fruta",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/mandarina-criolla-xkg/_/R-00000501-00000501-200?Dy=1",
                # "Dia": "",
                "Jumbo": "https://www.jumbo.com.ar/mandarina-criolla-1-kg/p",
                "Carrefour": "https://www.carrefour.com.ar/mandarina-x-kg/p"
                
                }
    },                           
        "mandarina_nova": {
        "nombre": "Mandarina Nova",        
        "unidad": "1",        
        "categoria": "Fruta",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/mandarina-nova-x-kg/_/R-00000204-00000204-200?Dy=1",
                # "Dia": "",
                "Jumbo": "https://www.jumbo.com.ar/mandarina-nova-x-kg/p",
                "Carrefour": "https://www.carrefour.com.ar/mandarina-nova-huella-natural-x-kg/p"
                
                }
    },                      
        "limon": {
        "nombre": "Limon",        
        "unidad": "1",        
        "categoria": "Fruta",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/limon-comercia-xkg/_/R-00061007-00061007-200?Dy=1",
                # "Dia": "",
                "Jumbo": "https://www.jumbo.com.ar/limon-x-kg/p",
                "Carrefour": "https://www.carrefour.com.ar/limon-comercial-x-kg/p"
                
                }
    },                         
        "kiwi": {
        "nombre": "Kiwi",        
        "unidad": "1",        
        "categoria": "Fruta",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/kiwi-selecci%C3%B3n-x-kg/_/R-00000496-00000496-200?Dy=1",
                # "Dia": "",
                "Jumbo": "https://www.jumbo.com.ar/kiwi-elegido-x-kg/p",
                "Carrefour": "https://www.carrefour.com.ar/kiwi-huella-natural-x-kg/p"
                
                }
    },                             
        "arandanos_solimeno": {
        "nombre": "Arandanos Solimeno",        
        "unidad": "0.5",        
        "categoria": "Fruta",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/frutas-congeladas-ar%C3%A1ndanos-solimeno-500g/_/R-00566036-00566036-200?Dy=1&assemblerContentCollection=%2Fcontent%2FShared%2FAuto-Suggest%20Panels",
                # "Dia": "",
                # "Jumbo": "",
                # "Carrefour": ""
                
                }
    },                                
        "arandanos_karinat": {
        "nombre": "Arandanos Karinat",        
        "unidad": "0.3",        
        "categoria": "Fruta",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/frutas-arandanos-karinat-doy-300-grm/_/R-00502889-00502889-200?Dy=1&assemblerContentCollection=%2Fcontent%2FShared%2FAuto-Suggest%20Panels",
                # "Dia": "",
                # "Jumbo": "",
                # "Carrefour": ""
                
                }
    },                                
        "arandanos_quillen": {
        "nombre": "Arandanos Quillen",        
        "unidad": "0.4",        
        "categoria": "Fruta",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/frutas-congeladas-ar%C3%A1ndanos-quillen-400g/_/R-00604305-00604305-200?Dy=1&assemblerContentCollection=%2Fcontent%2FShared%2FAuto-Suggest%20Panels",
                # "Dia": "",
                # "Jumbo": "",
                # "Carrefour": ""
                
                }
    },                                
        "nuez_cascara": {
        "nombre": "Nuez con Cascara",        
        "unidad": "1",        
        "categoria": "Fruta",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/nuez-grande-c-cascar-xkg/_/R-00017749-00017749-200?Dy=1",
                # "Dia": "",
                "Jumbo": "https://www.jumbo.com.ar/nuez-con-cascara-premium-por-kg/p",
                # "Carrefour": ""
                
                }
    },                                   
        "yogurt_ilolay_vainilla": {
        "nombre": "Yogurt Ilolay Vainilla 900  gr",        
        "unidad": "0.9",        
        "categoria": "Lacteo",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/yogur-entero-ilolay-vainilla-bebible-900g/_/R-00013922-00013922-200",
                # "Dia": "",
                "Jumbo": "https://www.jumbo.com.ar/yogur-vainilla-sachet-x-900-gr-ilolay/p",
                # "Carrefour": ""
                
                }
    },                                      
        "yogurt_ilolay_vainilla_descremado": {
        "nombre": "Yogurt Ilolay Vainilla Descremado",        
        "unidad": "1",        
        "categoria": "Lacteo",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/yogur-descremado-ilolay-vainilla-bebible-1kg/_/R-00483171-00483171-200",
                # "Dia": "",
                # "Jumbo": "",
                # "Carrefour": ""
                
                }
    },                                         
        "yogurt_ilolay_frutilla_descremado": {
        "nombre": "Yogurt Ilolay Frutilla Descremado",        
        "unidad": "1",        
        "categoria": "Lacteo",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/yogur-descremado-ilolay-frutilla-bebible-1kg/_/R-00483170-00483170-200",
                # "Dia": "",
                # "Jumbo": "",
                # "Carrefour": ""
                
                }
    },                                         
        "yogurt_ilolay_frutilla_descremado": {
        "nombre": "Yogurt Ilolay Frutilla Descremado 900 gr",        
        "unidad": "0.9",        
        "categoria": "Lacteo",
        "urls": {
                # "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/yogur-descremado-ilolay-frutilla-bebible-1kg/_/R-00483170-00483170-200",
                # "Dia": "",
                "Jumbo": "https://www.jumbo.com.ar/yogur-descremado-frutilla-sachet-x-900-gr-ilolay/p",
                "Carrefour": "https://www.carrefour.com.ar/yogur-bebible-descremado-de-frutilla-ilolay-en-sachet-900-g-739069/p"
                
                }
    },                                           
        "yogurt_ilolay_durazno": {
        "nombre": "Yogurt Ilolay Durazno",        
        "unidad": "1",        
        "categoria": "Lacteo",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/yogur-ilolay-durazno-bebible-1kg/_/R-00483169-00483169-200",
                # "Dia": "",
                # "Jumbo": "",
                # "Carrefour": ""
                
                }
    },                                      
        "yogurt_ilolay_frutilla_kiwi": {
        "nombre": "Yogurt Ilolay Frutilla kiwi",        
        "unidad": "0.9",        
        "categoria": "Lacteo",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/yogur-bebible-parcialmente-descremado-frutilla-kiwi-ilolay-900-gr/_/R-00546792-00546792-200",
                # "Dia": "",
                # "Jumbo": "",
                # "Carrefour": ""
                }
    },                                         
        "yogurt_milkaut_vainilla_descremado": {
        "nombre": "Yogurt Milkaut Vainilla Descremado",        
        "unidad": "0.9",        
        "categoria": "Lacteo",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/yogur-bebible-descremado-sabor-vainilla-milkaut-900g/_/R-00562336-00562336-200?Dy=1&idSucursal=200",
                # "Dia": "",
                "Jumbo": "https://www.jumbo.com.ar/yogur-milkaut-balance-vainilla-900g/p",
                "Carrefour": "https://www.carrefour.com.ar/yogur-descremado-milkaut-de-vainilla-en-sachet-900-g-719267/p"
                }
    },                                         
        "yogurt_milkaut_vainilla_fortificado_300": {
        "nombre": "Yogur Bebible Entero Fortificado Vainilla MILKAUT 1,2 Kg",        
        "unidad": "1.2",        
        "categoria": "Lacteo",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/yogur-bebible-entero-fortificado-vainilla-milkaut-1-2-kg/_/R-00511818-00511818-200?Dy=1",
                # "Dia": "",
                "Jumbo": "https://www.jumbo.com.ar/yogur-milkaut-entero-vainilla-x-1-2-kg/p",
                # "Carrefour": ""
                }
    },                                            
        "yogurt_milkaut_descremado_frutilla": {
        "nombre": "Yogur Bebible Descremado Frutilla",        
        "unidad": "0.9",        
        "categoria": "Lacteo",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/yogur-bebible-descremado-sabor-frutilla-milkaut-900g/_/R-00562324-00562324-200?Dy=1",
                # "Dia": "",
                "Jumbo": "https://www.jumbo.com.ar/yogur-milkaut-balance-frutilla-900g/p",
                "Carrefour": "https://www.carrefour.com.ar/yogur-descremado-milkaut-de-frutilla-en-sachet-900-g-719266/p"
                }
    },                                            
        "yogurt_milkaut_durazno": {
        "nombre": "Yogurt Milkaut Durazno",        
        "unidad": "0.9",        
        "categoria": "Lacteo",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/yogur-bebible-entero-durazno-milkaut-sch-900-grm/_/R-00521116-00521116-200?Dy=1",
                # "Dia": "",
                "Jumbo": "https://www.jumbo.com.ar/yogur-milkaut-durazno-sachet-900-g/p",
                "Carrefour": "https://www.carrefour.com.ar/yogur-entero-milkaut-de-durazno-en-sachet-900-g-686542/p"
                }
    },                                            
        "yogurt_milkaut_vainilla": {
        "nombre": "Yogurt Milkaut Vainilla",        
        "unidad": "0.9",        
        "categoria": "Lacteo",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/yogur-bebible-entero-vainilla-milkaut-sch-900-grm/_/R-00521115-00521115-200?Dy=1",
                "Dia": "https://diaonline.supermercadosdia.com.ar/yogur-entero-vainilla-sachet-milkaut-900-gr-304360/p",
                "Jumbo": "https://www.jumbo.com.ar/yogur-milkaut-vainilla-sachet-900-g-2/p",
                "Carrefour": "https://www.carrefour.com.ar/yogur-entero-milkaut-vainilla-sachet-900-g/p"
                }
    },                                            
        "yogurt_milkaut_frutilla_fortificado": {
        "nombre": "Yogurt Milkaut Frutilla Fortificado",        
        "unidad": "1.25",        
        "categoria": "Lacteo",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/yog-beb-ent-fort-fru-milkaut-sch-1250-kgm/_/R-00510422-00510422-200?Dy=1",
                # "Dia": "",
                "Jumbo": "https://www.jumbo.com.ar/yogur-milkaut-bebible-sabor-frutilla-x-1-2-kg/p",
                "Carrefour": "https://www.carrefour.com.ar/yogur-bebible-frutilla-milkaut-sachet-125-kg/p"
                }
    },                                            
        "casancrem_grande": {
        "nombre": "Casancrem 500 gr",        
        "unidad": "0.5",        
        "categoria": "Lacteo",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/queso-crema-cl%C3%A1sico-casancrem-500gr/_/R-00592566-00592566-200?Dy=1",
                "Dia": "https://diaonline.supermercadosdia.com.ar/queso-crema-clasico-casancrem-500-gr-2797/p",
                "Jumbo": "https://www.jumbo.com.ar/queso-crema-clasico-500-gr-casancrem/p",
                "Carrefour": "https://www.carrefour.com.ar/queso-crema-casancrem-clasico-500-grs-748003/p"
                }
    },                                            
        "casancrem_chico": {
        "nombre": "Casancrem 290 gr",        
        "unidad": "0.29",        
        "categoria": "Lacteo",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/queso-crema-cl%C3%A1sico-casancrem-290gr/_/R-00572016-00572016-200?Dy=1",
                "Dia":"https://diaonline.supermercadosdia.com.ar/queso-crema-clasico-casancrem-290-gr-298788/p",
                "Jumbo": "https://www.jumbo.com.ar/queso-blanco-balance-290-gr-casancrem/p",
                "Carrefour": "https://www.carrefour.com.ar/queso-crema-clasico-casancrem-290-g-726373/p"
                }
    },                                            
        "manteca_chica_serenisima": {
        "nombre": "Manteca La Serenisima 100 gr",        
        "unidad": "0.1",        
        "categoria": "Lacteo",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/manteca-la-serenisima-100gr/_/R-00003817-00003817-200?Dy=1",
                "Dia":"https://diaonline.supermercadosdia.com.ar/manteca-la-serenisima-100-gr-60589/p",
                "Jumbo": "https://www.jumbo.com.ar/manteca-ls-bienestar-animal-200-g/p",
                "Carrefour": "https://www.carrefour.com.ar/manteca-la-serenisima-clasica-100-g-267020/p"
                
                }
    },                                            
        "manteca_grande_serenisima": {
        "nombre": "Manteca La Serenisima 200 gr",        
        "unidad": "0.2",        
        "categoria": "Lacteo",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/manteca-la-serenisima-200gr/_/R-00003818-00003818-200?Dy=1",
                "Dia":"https://diaonline.supermercadosdia.com.ar/manteca-la-serenisima-200-gr-14938/p",
                "Jumbo": "https://www.jumbo.com.ar/manteca-ls-bienestar-animal-200-g/p",
                "Carrefour": "https://www.carrefour.com.ar/manteca-la-serenisima-extra-para-untar-200-g/p"
                }
    },                                            
        "queso_rallado_serenisima_130": {
        "nombre": "Queso Rallado La Serenisima 130 gr",        
        "unidad": "0.13",        
        "categoria": "Lacteo",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/queso-rallado-reggianito-la-serenisima-130g/_/R-00510760-00510760-200?Dy=1",
                "Dia":"https://diaonline.supermercadosdia.com.ar/queso-reggianito-rallado-la-serenisima-130-gr-273230/p",
                "Jumbo": "https://www.jumbo.com.ar/queso-reggianito-rallado-la-serenisima-130-gr/p",
                "Carrefour": "https://www.carrefour.com.ar/queso-rallado-reggianito-la-serenisima-bolsa-130-g/p"
                }
    },                                            
        "queso_rallado_serenisima_175": {
        "nombre": "Queso Rallado La Serenisima 175 gr",        
        "unidad": "0.175",        
        "categoria": "Lacteo",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/queso-rallado-reggianito-la-serenisima-175g/_/R-00510763-00510763-200?Dy=1",
                # "Dia":"",
                "Jumbo": "https://www.jumbo.com.ar/queso-reggianito-rallado-la-serenisima-175gr/p",
                "Carrefour": "https://www.carrefour.com.ar/queso-rallado-la-serenisima-reggianito-flow-pack-175-g/p"
                }
    },                                            
        "leche_3_ninas": {
        "nombre": "Leche Larga Vida Las tres Ninas",        
        "unidad": "1",        
        "categoria": "Lacteo",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/leche-larga-vida-entera-las-tres-ni%C3%B1as-ttb-1l/_/R-00254550-00254550-200",
                "Dia":"https://diaonline.supermercadosdia.com.ar/leche-entera-las-3-ninas-larga-vida-1-lt-58463/p",
                "Jumbo": "https://www.jumbo.com.ar/leche-uat-entera-las-tres-ninas-1l/p",
                "Carrefour": "https://www.carrefour.com.ar/leche-entera-larga-vida-las-tres-ninas-1-l/p"
                }
    },                                            
        "leche_serenisima": {
        "nombre": "Leche Larga Vida La Serenisima",        
        "unidad": "1",        
        "categoria": "Lacteo",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/leche-larga-vida-entera-ua-clasica-3-la-serenisima-1l/_/R-00251875-00251875-200",
                "Dia":"https://diaonline.supermercadosdia.com.ar/leche-larga-vida-clasica-3--la-serenisima-1-lt-295999/p",
                "Jumbo": "https://www.jumbo.com.ar/leche-uat-serenisima-3-1-lt/p",
                "Carrefour": "https://www.carrefour.com.ar/leche-la-serenisima-clasica-3-1l-720719/p"
                }
    },                                            
        "bizcochuelo_morixe": {
        "nombre": "Bizcochuelo Morixe Chocolate",        
        "unidad": "0.540",        
        "categoria": "Almacen",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/bizcochuelo-sabor-chocolate-morixe-540-grm/_/R-00541561-00541561-200?Dy=1",
                "Dia": "https://diaonline.supermercadosdia.com.ar/bizcochuelo-chocolate-morixe-540-gr-1072/p",
                "Jumbo": "https://www.jumbo.com.ar/bizcochuelo-chocolate-morixe-540-gr/p",
                "Carrefour": "https://www.carrefour.com.ar/bizcochuelo-morixe-de-chocolate-540-g-705873/p"
                }
    },                                            
        "arroz_molinos_ala_grande": {
        "nombre": "Arroz Molinos Ala 1 Kg",        
        "unidad": "1",        
        "categoria": "Almacen",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/arroz-largo-fino-molinos-ala-paquete-1-kg/_/R-00002270-00002270-200?Dy=1",
                "Dia": "https://diaonline.supermercadosdia.com.ar/arroz-largo-fino-ala-1-kg-25417/p",
                "Jumbo": "https://www.jumbo.com.ar/arroz-ala-grano-largo-fino-1-kg/p",
                "Carrefour": "https://www.carrefour.com.ar/arroz-largo-fino-molinos-ala-1-kg/p"
                }
    },                                            
        "arroz_molinos_ala_chico": {
        "nombre": "Arroz Molinos Ala 500 gr",        
        "unidad": "0.5",        
        "categoria": "Almacen",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/arroz-largo-fino-molinos-ala-paquete-500-gr/_/R-00029048-00029048-200?Dy=1&idSucursal=200",
                "Dia": "https://diaonline.supermercadosdia.com.ar/arroz-largo-fino-molinos-ala-500-gr-298635/p",
                "Jumbo": "https://www.jumbo.com.ar/arroz-ala-grano-largo-fino-500-gr/p",
                "Carrefour": "https://www.carrefour.com.ar/arroz-molinos-ala-largo-fino-00000-bolsa-500-g/p"
                }
    },                                            
        "harina_pizza_morixe": {
        "nombre": "Harina 0000 Morixe",        
        "unidad": "1",        
        "categoria": "Almacen",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/harina-trigo-0000-morixe-1kg/_/R-00480052-00480052-200?Dy=1",
                "Dia": "https://diaonline.supermercadosdia.com.ar/harina-0000-morixe-1-kg-258543/p",
                "Jumbo": "https://www.jumbo.com.ar/harina-0000-morixe-1-kg/p",
                "Carrefour": "https://www.carrefour.com.ar/harina-de-trigo-morixe-0000-1-kg/p"
                }
    },                                            
        "harina_pizza_favorita": {
        "nombre": "Harina 0000 Favorita",        
        "unidad": "1",        
        "categoria": "Almacen",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/harina-trigo-0000-fortificado-con-hierro-favorita-1kg/_/R-00577876-00577876-200?Dy=1",
                "Dia": "https://diaonline.supermercadosdia.com.ar/harina-0000-con-vitaminas-favorita-1-kg-300779/p",
                "Jumbo": "https://www.jumbo.com.ar/harina-0000-vit-x-1-kg-favorita/p",
                "Carrefour": "https://www.carrefour.com.ar/harina-de-trigo-0000-favorita-fortificada-1-kg-733197/p"
                }
    },                                            
        "harina_pizza_blancaflor": {
        "nombre": "Harina 0000 Blancaflor",        
        "unidad": "1",        
        "categoria": "Almacen",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/harina-trigo-0000-blancaflor-1kg/_/R-00581616-00581616-200?Dy=1",
                # "Dia": "",
                "Jumbo": "https://www.jumbo.com.ar/harina-0000-fort-blancaflor-x-1kg/p",
                "Carrefour": "https://www.carrefour.com.ar/harina-de-trigo-0000-blancaflor-1-kg-735295/p"
                }
    },                                            
        "harina_pizza_pureza": {
        "nombre": "Harina 0000 Pureza",        
        "unidad": "1",        
        "categoria": "Almacen",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/harina-de-trigo-pureza-0000-paquete-1-kg/_/R-00253696-00253696-200?Dy=1",
                "Dia": "https://diaonline.supermercadosdia.com.ar/harina-0000-pureza-ultra-refinada-1-kg-167177/p",
                "Jumbo": "https://www.jumbo.com.ar/harina-pureza-ultra-refinada-1-kg/p",
                "Carrefour": "https://www.carrefour.com.ar/harina-de-trigo-pureza-0000-1-kg-551284/p"
                }
    },                                            
        "tomate_lata_campanola": {
        "nombre": "Tomate Perita La Campanola Lata",        
        "unidad": "0.4",        
        "categoria": "Almacen",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/tomate-perita-la-campagnola-lata-400-gr/_/R-00046126-00046126-200?Dy=1",
                "Dia": "https://diaonline.supermercadosdia.com.ar/tomate-pelado-perita-la-campagnola-400-gr-59422/p",
                # "Jumbo": "",
                # "Carrefour": ""
                }
    },                                            
        "lentejas_genericas": {
        "nombre": "Lentejas Genericas",        
        "unidad": "0.4",        
        "categoria": "Almacen",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/lentejas-coto-bolsa-400-gr/_/R-00171605-00171605-200?Dy=1",
                "Dia": "https://diaonline.supermercadosdia.com.ar/lentejas-dia-400-gr-292388/p",
                "Jumbo": "https://www.jumbo.com.ar/lentejas-secas-400-grs-cuisine-co/p",
                "Carrefour": "https://www.carrefour.com.ar/lentejas-carrefour-classic-400-g-738618/p"
                }
    },                                            
        "lentejas_elio": {
        "nombre": "Lentejas Don Elio",        
        "unidad": "0.4",        
        "categoria": "Almacen",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/lentejas-elio-bolsa-400-gr/_/R-00027685-00027685-200?Dy=1",
                # "Dia": "",
                # "Jumbo": "",
                # "Carrefour": ""
                }
    },                                            
        "polenta_morixe": {
        "nombre": "Polenta Morixe",        
        "unidad": "1",        
        "categoria": "Almacen",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/polenta-morixe-1kg/_/R-00511516-00511516-200?Dy=1",
                # "Dia": "",
                # "Jumbo": "",
                "Carrefour": "https://www.carrefour.com.ar/polenta-instantanea-morixe-paquete-1-kg/p"
                }
    },                                            
        "polenta_presto": {
        "nombre": "Polenta Presto Pronta",        
        "unidad": "0.730",        
        "categoria": "Almacen",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/polenta-instantanea-presto-pronta-paq-730-grm/_/R-00532414-00532414-200?Dy=1",
                "Dia": "https://diaonline.supermercadosdia.com.ar/polenta-instantanea-prestopronta-730-gr-285636/p",
                # "Jumbo": "",
                "Carrefour": "https://www.carrefour.com.ar/polenta-instantanea-presto-pronta-bolsa-730-g-697807/p"
                 }
    },                                            
        "higienico_higienol": {
        "nombre": "Papel Higiénico HIGIENOL Plus Doble Hoja 20 M 4 Un",        
        "unidad": "4 Unidades x 20 mts",        
        "categoria": "Limpieza",
        "urls": {
                "Coto": "https://www.cotodigital.com.ar/sitios/cdigi/productos/papel-higi%C3%A9nico-higienol-plus-doble-hoja-20-m-4-un/_/R-00588926-00588926-200?Dy=1",
                # "Dia": "",
                "Jumbo": "https://www.jumbo.com.ar/papel-higienico-plus-doble-hoja-20-m-x-4-un-higienol/p",
                "Carrefour": "https://www.carrefour.com.ar/papel-higienico-higienol-plus-doble-hoja-20-mts-4-uni-742467/p"
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
                "Carrefour": "https://www.carrefour.com.ar/papel-higienico-doble-hoja-higienol-plus-30-mts-18-uni-761669/p",
                # "Dia": "",
                # "Jumbo": "",
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
                # "Dia": "",
                # "Jumbo": "",
                 "Carrefour": "https://www.carrefour.com.ar/papel-higienico-doble-hoja-felpita-infinity-4-u-x-30-m/p"
                 }
    },                                            
        "higienico_jumbo": {
        "nombre": "Papel Higienico Doble Hoja 4x30 M Family Care Mp",        
        "unidad": "4 Unidades x 30 mts",        
        "categoria": "Limpieza",
        "urls": {
                "Jumbo":"https://www.jumbo.com.ar/papel-higienico-doble-hoja-4x30-m-family-care-mp-2/p",
                # "Dia": "",
                # "Jumbo": "",
                # "Carrefour": ""
                 }
    },                                            
        "higienico_dia": {
        "nombre": "Papel Higiénico Doble Hoja 30 mts 4 Ud.",        
        "unidad": "4 Unidades x 30 mts",        
        "categoria": "Limpieza",
        "urls": {
                "Dia":"https://diaonline.supermercadosdia.com.ar/papel-higienico-doble-hoja-30-mts-4-ud-16949/p",
                # "Dia": "",
                # "Jumbo": "",
                # "Carrefour": ""
                 }
    },                                            
        "higienico_dia_grande": {
        "nombre": "Papel Higiénico Doble Hoja 30mts 6 Ud",        
        "unidad": "6 Unidades x 30 mts",        
        "categoria": "Limpieza",
        "urls": {
                "Dia":"https://diaonline.supermercadosdia.com.ar/papel-higienico-doble-hoja-30mts-6-ud-834/p",
                # "Dia": "",
                # "Jumbo": "",
                # "Carrefour": ""
                 }
    },                                            
        "higienico_carrefour": {
        "nombre": "Papel higiénico doble hoja Carrefour Essential 4 x 30 mts",        
        "unidad": "6 Unidades x 30 mts",        
        "categoria": "Limpieza",
        "urls": {
                "Carrefour":"https://www.carrefour.com.ar/papel-higienico-doble-hoja-carrefour-essential-4-x-30-mts-597038/p",
                # "Dia": "",
                # "Jumbo": "",
                # "Carrefour": ""
                 }
    },                                            
        "higienico_carrefour_decorado": {
        "nombre": "Papel higiénico doble hoja deco Carrefour Essential 50 mts. x 4 uni",        
        "unidad": "6 Unidades x 50 mts",        
        "categoria": "Limpieza",
        "urls": {
                "Carrefour":"https://www.carrefour.com.ar/papel-higienico-doble-hoja-deco-carrefour-essential-50-mts-x-4-uni/p",
                # "Dia": "",
                # "Jumbo": "",
                # "Carrefour": ""
                 }
    },                                            
        "higienico_noble": {
        "nombre": "Papel higiénico Noble doble hoja 30 mts 4 uni",        
        "unidad": "4 Unidades x 30 mts",        
        "categoria": "Limpieza",
        "urls": {
                "Carrefour":"https://www.carrefour.com.ar/papel-higienico-noble-doble-hoja-30-mts-4-uni-751386/p",
                # "Dia": "",
                # "Jumbo": "",
                # "Carrefour": ""
                 }
    },                                            
        "higienico_elegante": {
        "nombre": "Papel higiénico doble hoja Elegante 4 x 30 m.",        
        "unidad": "4 Unidades x 30 mts",        
        "categoria": "Limpieza",
        "urls": {
                "Carrefour":"https://www.carrefour.com.ar/papel-higienico-doble-hoja-elegante-4-x-30-m-628282/p",
                # "Dia": "",
                # "Jumbo": "",
                # "Carrefour": ""
                 }
    },                                            
        "higienico_elegante_rinde": {
        "nombre": "Papel higiénico Elegante hoja doble rindemas 30 mts. x 4 uni",        
        "unidad": "4 Unidades x 30 mts",        
        "categoria": "Limpieza",
        "urls": {
                "Carrefour":"https://www.carrefour.com.ar/papel-higienico-elegante-hoja-doble-rindemas-30-mts-x-4-uni-702838/p",
                # "Dia": "",
                # "Jumbo": "",
                # "Carrefour": ""
                
                 }
    },                                           
        "rollo_cocina_campanita": {
        "nombre": "Rollo Cocina Campanita 100 panios",        
        "unidad": "2 Unidades x 100 panios",        
        "categoria": "Limpieza",
        "urls": {
                "Coto":"https://www.cotodigital.com.ar/sitios/cdigi/productos/rollo-de-cocina-campanita-100-pa%C3%B1os-paquete-2-unidades/_/R-00272112-00272112-200?Dy=1",
                # "Dia": "",
                # "Jumbo": "",
                # "Carrefour": ""
                

                 }
    },                                           
        "rollo_cocina_sussex": {
        "nombre": "Rollo Cocina Sussex 50 panios",        
        "unidad": "3 Unidades x 50 panios",        
        "categoria": "Limpieza",
        "urls": {
                "Coto":"https://www.cotodigital.com.ar/sitios/cdigi/productos/rollo-cocina-sussex-cl%C3%A1sico-50-pa%C3%B1os-3-un/_/R-00562930-00562930-200?Dy=1&idSucursal=200",
                "Jumbo": "https://www.jumbo.com.ar/rollo-cocina-clasico-50-panos-3-un-sussex/p",
                "Dia": "https://diaonline.supermercadosdia.com.ar/rollo-cocina-sussex-clasico-50-panos-3-ud-88515/p",
                "Carrefour": "https://www.carrefour.com.ar/rollo-de-cocina-sussex-clasico-50-panos-3-uni-719939/p"
                 }
    },                                           
        "rollo_cocina_sussex2": {
        "nombre": "Rollo Cocina Sussex 180 panios",        
        "unidad": "3 Unidades x 100 panios",        
        "categoria": "Limpieza",
        "urls": {
                "Coto":"https://www.cotodigital.com.ar/sitios/cdigi/productos/rollo-de-cocina-sussex-ultra-60-pa%C3%B1os-3-un/_/R-00580697-00580697-200?Dy=1",
                # "Dia": "",
                # "Jumbo": "",
                # "Carrefour": "https://www.carrefour.com.ar/rollo-de-cocina-sussex-ultra-60-panos-3-uni-735468/p"
                
                
                 }
    },                                         
        "rollo_cocina_sussex3": {
        "nombre": "Rollo Cocina Sussex 100 panios",        
        "unidad": "3 Unidades x 100 panios",        
        "categoria": "Limpieza",
        "urls": {
                "Jumbo":"https://www.jumbo.com.ar/rollo-de-cocina-ultra-100-panos-3-un-sussex/p",
                # "Dia": "",
                "Jumbo": "https://www.jumbo.com.ar/rollo-de-cocina-ultra-100-panos-3-un-sussex/p",
                "Carrefour": "https://www.carrefour.com.ar/rollo-de-cocina-sussex-ultra-100-panos-3-uni-578816/p"
                
                
                 }
    }




}