import cv2

# Cargar el clasificador preentrenado de Haar para detección de rostros
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Cargar la imagen en la que quieres detectar el rostro
image = cv2.imread('face2.jpg')

# Convertir la imagen a escala de grises (mejora el rendimiento)
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detectar los rostros en la imagen
faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

# Dibujar las cajas delimitadoras alrededor de los rostros detectados
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)  # Rojo para las cajas

# Mostrar la imagen con las detecciones
cv2.imshow("Rostros detectados", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Guardar la imagen con los rostros detectados
cv2.imwrite("imagen_detectada.jpg", image)