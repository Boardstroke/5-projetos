from PIL import Image
import numpy as np
import math as math

asc = '`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$'
size = 128,128



def get_asc(x):
    letter  = math.floor(0.65 * x)
    return letter

# Abrir uma imagem
try:
    im = Image.open('./eu.jpg')
    im.thumbnail(size, Image.ANTIALIAS)
    print("ok")
    
except:
    print("Erro")
else:
    # Transformar cada pixel da imagem em um array e armazenar em uma matriz

    s = np.asarray(im)
    print(s.shape)
    im_n = []
    #Cada elemento da matriz s é um pixel

    for i in range(len(s)):
        for j in range(len(s[i])):
            pixel  = s[i][j]
            brilho = (pixel[0] + pixel[1] + pixel[2]) / 3
            im_n.append(asc[get_asc(brilho)])
        

    mtr = np.reshape(im_n,(128,128))
    print(mtr.shape)

    for i in range(len(mtr)):
        for j in range(len(mtr[i])):
            print(mtr[i][j], end=' ') 

        print(' ')
