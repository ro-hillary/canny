import cv2
import numpy as np
import pydicom

# Cargar imagen dcm con pydicom
dcm = pydicom.dcmread('0003.DCM')
#Obtenemos la matriz de pixeles de la imagen
pixels = dcm.pixel_array[0]
#Convertimos la imagen a una matriz numpy de 8 bits
img = np.uint8(pixels)
# Aplicar algoritmo Canny
edges = cv2.Canny(img, 40, 60)
# Mostrar resultados
cv2.imshow('Imagen original', img)
cv2.imshow('Algoritmo Canny', edges)

cv2.waitKey(0)
cv2.destroyAllWindows()
