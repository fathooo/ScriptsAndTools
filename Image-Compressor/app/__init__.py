import os
from app.appConfig import createConfig
from app.imgCompressor import compressImagesInit


import os
from PIL import Image



def init():
    try: 
        print("Iniciando...")
        config = createConfig()
        if not config:
            raise Exception("Error config: verificar la configuración")
        images = compressImagesInit(os.getcwd())
        if not images:
            raise Exception("Error images: verificar las imagenes")
        print("Finalizado")
        return True
    except Exception as e:
        print(e)
        return False

