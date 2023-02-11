import shutil
import os


def removeDirectory(path):
    shutil.rmtree(path)


def createFolder(path):
    os.mkdir(path, 0o666)


def createSellerFolders(id):
    path = './static/sellerData/'
    createFolder(path+id)
    createFolder(path+id+"/product")


def saveImg(pic, path, name):
    extension = getImgExtensionByImgFilename(pic.filename)
    pic.save(os.path.join(path, name+"."+extension))


def getImgExtensionByImgFilename(name):
    lst=name.split('.')
    return lst[len(lst)-1]