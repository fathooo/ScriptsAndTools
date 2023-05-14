import os
from app.appConfig import FOLDERNAMETOSAVEIMAGES
from PIL import Image
import subprocess

#list format of images
formatImages = [".jpg", ".png", ".jpeg", "jfif"]

## create list of images in directory
def getImages(directory):
    try : 
        images = []
        for file in os.listdir(directory):
            if file.endswith(tuple(formatImages)):
                images.append(file)
        if images == []:
            raise Exception("No hay imagenes en el directorio")
        return images
    except Exception as e:
        print("funcError(getImages): " + str(e))
        return images

def compressImage(image, directory):
    try:
        imgPath = directory + "\\" + image
        img = Image.open(imgPath)
        toSavePath = "{}/{}/{}".format(directory, FOLDERNAMETOSAVEIMAGES, image)

        img.save(toSavePath, optimize=True, quality=75)
        print("---> Imagen comprimida: " + image)
        return True
    except Exception as e:
        print("funcError(compressImage): " + str(e))
        return False

def optimizeImages():
    try:
        subprocess.run(["optimize-images", "./{}".format(FOLDERNAMETOSAVEIMAGES)])
        print("Imagenes optimizadas")
        return True
    except Exception as e:
        print("funcError(optimizeImages): " + str(e))
        return False

def compressImagesInit(directory):
    try:
        print("-------------------------")
        print("Comprimiendo imagenes...")
        print("")
        images = getImages(directory)
        for image in images:
            compressImage(image, directory)
        print("")
        print("Optimizando imagenes...")
        print("")
        optimizeImages()
        print("")
        print("Optimizando imagenes finalizado")
        return True
    except Exception as e:
        print("funcError(compressImagesInit): " + str(e))
        return False
    