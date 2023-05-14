import os
from configparser import ConfigParser
from pytube import YouTube

FOLDER = "./files"
FILECONFIG = "./config.ini"
THISPATH = ".\\"

def verifyFolder():
    try:
        if not os.path.exists(FOLDER):
            os.mkdir(FOLDER)
        return True
    except:
        return False

def verifyConfig():
    try:
        os.chdir(THISPATH)
        config = ConfigParser()
        if not os.path.exists(FILECONFIG):
            config['DEFAULT'] = {'filesDir': False,
                                 'pathDir': ".\\" }
            with open('config.ini', 'w') as configfile:
                config.write(configfile)

        config.read(FILECONFIG)

        if config['DEFAULT']['filesDir'] == "True":
            os.chdir(config['DEFAULT']['pathDir'])
            
        verifyFolder()
        print("Directorio actual: ", os.getcwd())
        return True
    except:
        return False

def downloadVideo(link):
    try:
        video = YouTube(link)
        descarga = video.streams.get_highest_resolution()
        descarga.download(FOLDER)
        return True
    except:
        return False

def init():
    try:
        if verifyConfig():
            print("Configuracion correcta")
        else:
            print("Configuracion incorrecta")

        link = input("Ingrese el link del video: ")
        if downloadVideo(link):
            print("Descarga exitosa")
        else:
            print("Error al descargar")
    except:
        print("Error en la ejecucion")

if __name__ == "__main__":
    init_ = init()
    input("Presione enter para salir")

