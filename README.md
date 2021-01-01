# Regularización
 
Esta técnica consiste en disminuir la complejidad de nuestro modelo a través de una penalización aplicada a sus variables más irrelevantes.
 
Entonces, la regularización consiste en introducir un poco de sesgo para reducir la varianza de los datos.
 
![14](https://user-images.githubusercontent.com/63415652/103431691-e0e33c00-4b99-11eb-860a-820e8b70bbc9.PNG)
  
Ahora vamos a ver cual técnica nos genera menos pérdida: 
 
![15](https://user-images.githubusercontent.com/63415652/103431748-f147e680-4b9a-11eb-99f6-87e7442d845b.PNG) 
 
Y como poder ver, la lineal genera menos pérdida. 
 
Ahora veremos los coeficientes:
 
![16](https://user-images.githubusercontent.com/63415652/103431890-10e00e80-4b9d-11eb-808d-5f32015a455a.PNG) 
 
Esto es un arreglo numérico que tiene el mismo tamaño de las columnas que utilizamos en nuestros features, esto es porque cada uno de los números corresponden uno a uno a las columnas que estamos intentando evaluar y aquí en donde podemos sacar más información relevante, porque cuando encontramos los números más grandes, directamente podemos saber que esa columna es la que más peso está teniendo en el modelo que estamos entrenando.
Por ejemplo en Lasso, el factor económico tiene mucho más peso que las demás variables que el índice de felicidad que se calcula y en este caso, Lasso decidió quitar las demás variables ya que nos las encontró determinantes. 
 
>**_Conclusión:_** Esto nos abre la puerta a muchas preguntas que tenemos que hacernos sobre nuestros datos, pero eso ya está a nuestro criterio entender esas relaciones complejas y hacer más pruebas para entender específicamente lo qué está pasando. 
 
# Regresiones robustas. 
 
Ransac: selecciona una muestra aleatoria de los datos asumiendo que esa muestra se encuentra dentro de los valores inliners, con estos datos se entrena el modelo y se compara su comportamiento con respecto a los otros datos. Este procedimiento se repite tantas veces como se indique y al finalizar el algoritmo escoge la combinación de datos que tenga la mejor cantidad de inliners, donde los valores atípicos puedan ser discriminados de forma efectiva.
 
![17](https://user-images.githubusercontent.com/63415652/103431940-d75bd300-4b9d-11eb-9ba2-5d549e0b440e.PNG)
 
Huber Reggresor: no elimina los valores atípicos sino que los penaliza. Realiza el entrenamiento y si el error absoluto de la pérdida alcanza cierto umbral (epsilon) los datos son tratados como atípicos. El valor por defecto de epsilon es 1.35 ya que se ha demostrado que logra un 95% de eficiencia estadística.
 
Ahora pasaremos a hacer una regresión robusta introduciendo algunos datos corruptos, para lidiar con ellos de una manera efectiva.
 
 
![18](https://user-images.githubusercontent.com/63415652/103432212-09226900-4ba1-11eb-9def-deac0a86ca20.PNG)
 
 
La modificación que se hizo fue agregar valores en nuestro dataset en ceros, de tal manera esto podría confundir a nuestros modelos si no están bien entrenados o si no hemos trabajado con esos valores atípicos antes 
 
Ahora vamos a aplicar Ransac y Huber:
 
![19](https://user-images.githubusercontent.com/63415652/103432432-4b00de80-4ba4-11eb-97df-38a34e4a0e6e.PNG) 
 
Como podemos ver en los resultados, tanto RANSAC como HUBER tienen un error mucho menor que la SVR. 
 
>**_Conclusión:_** Aquí claramente podemos ver como los valores atípicos si afectan el desempeño de nuestro modelo, por lo tanto siempre será importante tomar alguna medida de precaución para poder lidiar con este proceso de una manera satisfactoria.  