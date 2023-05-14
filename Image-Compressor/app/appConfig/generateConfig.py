#%%
import os
from configparser import ConfigParser


FILECONFIG = os.path.dirname(os.path.abspath(__file__)) + "/config.ini" # Path to config file
FOLDERNAMETOSAVEIMAGES = "Imagescompressed" # Folder to save images compressed
FOLDERNAMETOSEARCH = "" # Folder to search images | Empty string to search in current folder
PATHTOSEARCH = str(os.getcwd())

CONFIG = ConfigParser() # init configfile

def verifyFolderToSaveImages():
    try:
        if len(FOLDERNAMETOSAVEIMAGES) > 0: 
            if not os.path.exists("./{}".format(FOLDERNAMETOSAVEIMAGES)):
                os.mkdir(FOLDERNAMETOSAVEIMAGES)
        return True
    except Exception as e:
        print(e)
        return False

def verifyFolderToSearchImages():
    try:
        if len(FOLDERNAMETOSEARCH) > 0: 
            if not os.path.exists("./{}".format(FOLDERNAMETOSEARCH)):
                os.mkdir(FOLDERNAMETOSEARCH)
        return True
    except Exception as e:
        print(e)
        return False

def inputSelectPath():
    try:
        print("")
        response = input("select a PATH to search images: \n")
        return response     
    except Exception as e:
        print(e)
        return False

def createConfigFileini():
    try:
        if not os.path.exists(FILECONFIG):
            response = inputSelectPath() # Select path to search images
            if len(response) > 0:
                CONFIG['DEFAULT'] = {
                    'ActivateOtherFolderSearch': 'True',
                    'PATHTOSEARCH': response
                }
            if len(response) == 0:
                CONFIG['DEFAULT'] = {
                    'ActivateOtherFolderSearch': 'False',
                    'PATHTOSEARCH': PATHTOSEARCH
                }

            with open(FILECONFIG, 'w') as configfile:
                CONFIG.write(configfile)
            return True
        return False
    except Exception as e:
        print("createConfigFileini: {e}".format(e))
        return False

def createConfig():
    try:
        createConfigFileini()
        if not os.path.exists(FILECONFIG):
            raise Exception("createConfig: No existe el archivo de configuración")
        CONFIG.read(FILECONFIG)
        if CONFIG['DEFAULT']['ActivateOtherFolderSearch'] == "True":
            os.chdir(CONFIG['DEFAULT']['pathtosearch'])
        print("Directorio actual: ", os.getcwd())
        verifyFolderToSaveImages()
        return True
    except Exception as e:
        print("funcError(createConfig): " + str(e))
        return False



