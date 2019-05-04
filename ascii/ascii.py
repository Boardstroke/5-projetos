import numpy as np 
import math as math
from PIL import Image
import sys as sys

if len(sys.argv) > 1:
    src = sys.argv[1]
else:
    src = 'mario.png'
asc = '`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$'

size = 128,128

class Imagem:
    def __init__(self, src):
        self.src = src
    
    def get_asc(self, x):
        letra = math.floor(0.15 * x)
        return letra
    
    def carregar_img(self):
        try:
            im = Image.open('./' + self.src)
            im.thumbnail(size, Image.ANTIALIAS)
            print(im.size[0])
            return im
        except:
            print('erro')
    
    def transformar(self):
        im = self.carregar_img()
        s = np.asarray(im)
        im_n = []

        for i in range(len(s)):
            for j in range(len(s[i])):
                pixel = s[i][j]
                brilho = max((pixel[0]  , pixel[1], pixel[2])) + min((pixel[0], pixel[1], pixel[2])) / 2
                im_n.append(asc[self.get_asc(brilho)])
        
        
        mtr = np.reshape(im_n,(im.size[1], im.size[0]))
        
        for i in range(len(mtr)):
            for j in range(len(mtr[i])):
                print(mtr[i][j], end=' ') 

            print(' ')
if __name__ == "__main__":
    teste =  Imagem(src)
    teste.transformar()

    #TODO:
        #converter a imagem em .jpg