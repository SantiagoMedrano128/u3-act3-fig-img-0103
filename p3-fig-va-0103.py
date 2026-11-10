import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import cv2

# Santiago Medrano NC 0103
print("Santiago Medrano NC 0103")
print("UIII Act3 colocar puntos a una imagen  en blanco y negro")
mi_imagen= cv2.imread('casa antigua.jpg')
plt.imshow(mi_imagen)
plt.title('Casa antigua, Santiago Medrano 0103')
plt.show()
print("-+-+-+-+- Puntos en la imagen -+-+-+-+-")
plt.imshow(mi_imagen)
x = [100,100,300,620]
y = [100,400,500,350]
plt.scatter(x, y, s=20,c = 'red')
plt.show()