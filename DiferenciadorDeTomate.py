import numpy as np
import cv2

imagem = cv2.imread("/home/theo/Imagens/tomateverde.jpg")
redimensionada = cv2.resize(imagem, (500, 500))
altura1, largura1, c1 = np.shape(redimensionada)
verde = 0
maduro = 0
soma = 0 
for i in range(0, 500):
    for j in range(0,500):
        (b1,g1,r1) = redimensionada[i,j]
        if (b1 != 255 and g1 != 255 and r1 != 255):
            (b,g,r) = redimensionada[i,j]
            media= (int(b) + int(g) + int(r) / 3)
            if abs(media - r) > abs(media - g):
                verde += 1
            elif abs(media - r) < abs(media - g):
                maduro += 1




if (maduro > verde):
    print("\n\nO tomate está maduro!!\n\n")
else:
    print("\n\nO tomate está verde!!\n\n")



pretoebranco = cv2.cvtColor(redimensionada, cv2.COLOR_BGR2GRAY )
_, th1 = cv2.threshold(pretoebranco, 200 ,255, cv2.THRESH_BINARY)
altura= 0
largura = 0
for i in range(0,500):
        if(th1[250,i] == 0):
            largura += 1

for i in range(0,500):
        if(th1[i,250] == 0):
            altura += 1

        



if(altura > largura):
    print("O tomate se encaixa mais no grupo do tipo italiano.\n\n")
else:
    print("O tomate se encaixa mais no grupo do tipo caqui.\n\n")



