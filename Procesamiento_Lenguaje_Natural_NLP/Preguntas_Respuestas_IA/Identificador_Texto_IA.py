# Primero se instala scikit-learn pandas con el siguiente comando "pip install scikit-learn pandas"
# Luego de bajar librerias, las importamos
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline

# Primero creamos textos de ejemplo y sus respectivas categorias
# Con esto entrenamos la inteligencia artifica
data = {
    'texto': [
        'Me gusta leer libros, A veces voy a las bibliotecas, libro texto pdf biblioteca',
        'es bueno el cine, Amo las películas de accion, pelicula cines videos terror documental',
        'La comida colombiana es deliciosa, Los jugos son refrescantes, comidas almuerzo almuerzos desayuno desayunos',
        'Los videojuegos son entretenidos, Los juegos de video son divertidos, juego entretenido entretenida divertido divertida play xbox computador',
        ' '
    ],
    'categoria': [
        'lectura',
        'cine',
        'comida',
        'videojuego',
        'vacio'
    ]
}

# Creamos en dataframe con las listas anteriormente creadas
df = pd.DataFrame(data)

# Dividimos el datagrame en características (X) y etiquetas (y)
X = df['texto']
y = df['categoria']

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Crear un pipeline que combine el vectorizador y el clasificador
model = make_pipeline(CountVectorizer(), MultinomialNB())

# Ingresamos los datos para entrenar el software
model.fit(X_train, y_train)

# Función para predecir la categoría de una nueva frase
def predecir_categoria(frase):
    prediccion = model.predict([frase])
    return prediccion[0]

# Ingresar una nueva frase y predecir su categoría
frase = input("Por favor, ingrese una frase para identificar su categoria: ")
categoria_predicha = predecir_categoria(frase)

print(f'La categoría de la frase es: {categoria_predicha}')
print(f'La frase es: {frase}')



