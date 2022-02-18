from PIL import Image, ImageDraw
from random import randint
import win32api, win32con, win32gui
from time import sleep
import os

def setWallpaper(path):
    key = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER,"Control Panel\\Desktop",0,win32con.KEY_SET_VALUE)
    win32api.RegSetValueEx(key, "WallpaperStyle", 0, win32con.REG_SZ, "0")
    win32api.RegSetValueEx(key, "TileWallpaper", 0, win32con.REG_SZ, "0")
    win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER, path, 1+2)

couleur = (randint(0, 255), randint(0, 255), randint(0, 255))
background = Image.open("BG2.jpg", "r")
pixels = background.getdata()
taille = background.size
print(taille)

while True:
    img = Image.new('RGB', (taille[0], taille[1]), color=0)
    dessinateur = ImageDraw.Draw(img)
    shade = ((couleur[0]+randint(20, 100)), (couleur[1]+randint(20, 100)), (couleur[2]+randint(20, 100)))
    print(shade)
    if couleur[0] >= 255 or couleur[1] >= 255 or couleur[2] >= 255:
        shade = (0, 0, 0)
    for x in range(taille[1]):
        for y in range(taille[0]):
            dessinateur.point((y, x), fill=(int((pixels[x*taille[0]+y][0] + 2*shade[0])/3), int((pixels[x*taille[0]+y][1] + 2*shade[1])/3), int((pixels[x*taille[0]+y][2] + 2*shade[2])/3)))
    img.save("fe.png", quality=100)
    setWallpaper(os.getcwd()+os.sep+'fe.png')
    sleep(5)