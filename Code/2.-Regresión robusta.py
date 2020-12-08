# Importamos pandas
import pandas as pd 
# Importamos sklearn y desde el modulo lineal importamos nuestros regressors 
from sklearn.linear_model import (
    RANSACRegressor, HuberRegressor
)
# Importamos el modulo de maquinas de soporte vectorial, que es el support vector regresor
from sklearn.svm import SVR 

# Importamos el módulo de entrenamiento
from sklearn.model_selection import train_test_split
# Importamos el error cuatratico medio 
from sklearn.metrics import mean_squared_error

if __name__ == "__main__":
    # Importamos nuestro dataset
    dataset = pd.read_csv('./data/felicidad_corrupt.csv')
    # Mostramos nuestro dataset
    print(dataset.head(5))
    # Definimos nuestro features quitando las columnas que no vamos a utilizar 
    # especificamos el eje 1 que es el de las columnas (0 para filas) y sacaremos 
    # el pais porque es un dato de texto y el score que es lo queremos predecir 
    X = dataset.drop(['country', 'score'], axis=1)
    # Y nuestros targets sera nuestra columna de score 
    y = dataset[['score']]

    # Partimos nuestros datos. Pasamos los features, nuestro target y el tamaño del conjuto de
    # entrenamiento, en este caso 30%. Para que la particion aleatoria sea siempre la misma 
    # utilizaremos random state, puede ser cualquier numero pero que sea el mismo 
    X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.3, random_state=42)

    # Definimos los estimadores con un diccionario 
    estimadores = {
        # Definimos la llave que es el nombre del estimador. Y el valor es la configuración de 
        # este estimador con los parámetros que requiera
        'SVR' : SVR(gamma= 'auto', C=1.0, epsilon=0.1),
        # Definimos a RANSAC como un meta estimador, ya que en los parametros podemos trabajar 
        # como estimadores de manera definida, pero por defecto usa regresion lineal 
        'RANSAC' : RANSACRegressor(),
        # Definimos HUBER y definimos el parametro epsilon asi sea el de defecto, solo para recordar 
        # que es configurable ya que si lo volvemos más pequeño muchos menos datos valores atipicos 
        # vamos a considerar 
        'HUBER' : HuberRegressor(epsilon=1.35)  
    } 


