# import las librerias necesarias con "pip install opencv-python cmake dlib"
import cv2
from numpy as np
import dlib

# En el siguiente codigo se selecciona el .dat que tiene los datos para entrenar la IA
# Tambien se guarda en una variable la imagen .jpg
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_69_face_landmarks.dat")
img = cv2.imread("face.jpg")

# Se escoge la imagen para hacerle la revision de rostros en ella
gray = cv2.cvtColor(src=img, code= cv2.COLOR_BGR2GRAY)
faces= detector(gray)

# Con este for se recorre la imagen buscando diferentes rostros
for face in faces:
    x1= face.left()
    y1= face.top()
    x2= face.right()
    y2= face.bottom()
    landmarks = predictor(image=gray, box=face)
    for n in range(0, 68):
        x = landmarks.part(n).x
        y = landmarks.part(n).y
        cv2.cicle(img= img, center=(x,y), radius=3, color=(0,255,0), thickness=-1)

# Se crea la imagen con los rostros resaltados en verde
cv2.imshow(winname="face", mat=img)
cv2.waitKey(delay=0)




