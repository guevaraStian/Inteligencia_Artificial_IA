#Es necesario descargar de la pagina https://www.microsoft.com/es-es/download/details.aspx?id=48137
#Es necesario descargar de pagina https://visualstudio.microsoft.com/es/downloads/  y descargar el visual
#Luego ejecutar la descarga de librerias pip install numpy opencv-python dlib imutils

from imutils import face_utils
import dlib
import cv2
 
# En el siguiente codigo se importa el .dat que tiene los datos para entrenar la IA
p = "shape_predictor_68_face_landmarks.dat"
detector = dlib.get_frontal_face_detector()
predicciones = dlib.shape_predictor(p)

captura = cv2.VideoCapture(0)
 
while True:
    # Con este codigo se lee la imagen que se va a analizar
    _, image = captura.read()
    gris = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
    # Se procede a detectar las lineas que representan caras
    rostros = detector(gris, 0)

    #Se determinan que partes de la imagen tienen caras con el siguiente for
    for (i, rostro) in enumerate(rostros):
        conformar = predicciones(gris, rostro)
        conformar = face_utils.shape_to_np(conformar)
    
        # Teniendo en cuenta donde estan las lineas que determinan una cara, se ponen puntos verdes 
        # Asi se indica donde estan los rostros
        for (x, y) in conformar:
            cv2.circle(image, (x, y), 2, (0, 255, 0), -1)
    
    # En el siguiente codigo, se muestra la imagen con los puntos verdes indicando los rostros
    cv2.imshow("Output", image)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
captura.release()