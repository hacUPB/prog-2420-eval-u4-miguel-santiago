[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/WQjBwS08)
# Introducción

Los archivos de texto y archivos de valores separados por comas (CSV) son dos formatos comunes de archivo que se utilizan para almacenar y compartir datos. Un archivo de texto es un archivo que contiene texto en formato de texto plano, que puede ser leído y editado por un ser humano. Estos archivos son útiles para almacenar información como documentos, correos electrónicos, o incluso código fuente. Por otro lado, un archivo CSV (Comma Separated Values) es un archivo que contiene datos en formato de tabla, donde cada fila representa una fila de datos y cada columna representa un campo de datos. Estos archivos son comunes en la mayoría de las aplicaciones de análisis de datos, como hojas de cálculo, bases de datos y sistemas de gestión de contenidos.

La importancia de saber utilizar archivos de texto y CSV a través de herramientas como Python es crucial en la programación. Python es un lenguaje de programación muy popular y versátil, que ofrece bibliotecas y módulos para trabajar con archivos de texto y CSV. Al aprender a utilizar estos formatos, los desarrolladores pueden crear aplicaciones que puedan leer y escribir archivos de texto y CSV, lo que les permite interactuar con grandes cantidades de datos y realizar análisis y procesamientos de datos. Además, la capacidad de trabajar con archivos de texto y CSV es fundamental en la creación de aplicaciones de análisis de datos, visualización de datos y machine learning. 

La Unidad 4 de nuestro curso de Programación se ha centrado en el análisis y procesamiento de datos provenientes de archivos. En esta evaluación, aplicaremos los conocimientos adquiridos a un escenario de la vida real: el trabajo con set de datos reales. 

## **Objetivo:**

La evaluación tiene como objetivo evaluar los conocimientos de los estudiantes en programación con Python, en particular en el manejo de archivos de texto y archivos de datos separados por comas (csv, *comma separated values*).

## **Requerimientos:**

La aplicación debe interactuar con el usuario y permitirle elegir las acciones a ejecutar, de la siguiente manera.
### **Menú Principal**

El menú principal debe mostrar tres posibles opciones: 

1. Listar archivos presentes en la ruta actual o ingresar una ruta donde buscar los archivos.
2. Procesar archivo de texto (.txt)
3. Procesar archivo separado por comas (.csv)
4. Salir

**Submenú para archivos de texto (.txt)**

- Debe proporcionar las siguientes opciones, donde cada opción llama a una **función** realizada para el caso específico:
    - **Contar número de palabras**: Debe contar el número de palabras en el archivo de texto y mostrar el resultado.
    - **Reemplazar una palabra por otra**: Debe permitir al usuario reemplazar una palabra por otra en el archivo de texto. La función debe recibir tanto la palabra a buscar, como la palabra por la que se tiene que reemplazar.
    - **Contar el número de caracteres:** El programa debe calcular dos valores. El primero es el número total de caracteres, incluidos los espacios en blanco, y el segundo es el número de caracteres sin contar los espacios en blanco. Ambos resultados deben ser mostrados.

**Submenú para archivos .csv**

- Debe proporcionar las siguientes opciones, donde cada opción llama a una **función** realizada para el caso específico:
    - **Mostrar las 15 primeras filas**: con el fin de tener un vistazo rápido del documento que se va a analizar, esta función le permite al usuario observar el contenido de las primeras 15 líneas del archivo. Así, el usuario podrá decidir sus próximas acciones.
    - **Calcular Estadísticas**: el usuario le pasa a la función cuál es la columna que quiere seleccionar, de ese modo, la función calcula el número de datos, el promedio, la mediana, el valor máximo y el mínimo de dicha columna y retorna el resultado, para ser mostrado en la función principal (*main()*).
    - **Graficar una columna completa con los datos**: Debe permitir al usuario elegir una columna de datos numéricos y mostrar una gráfica con los datos.

**Otras opciones**

- Los estudiantes deben discutir con el profesor otras opciones posibles que pueden ser útiles para trabajar con archivos de texto y archivos .csv.

# **Evaluación**

La evaluación se realizará con base en la implementación correcta de los requerimientos mencionados anteriormente. Se evaluarán los siguientes aspectos:

- Correcta implementación de la lógica de programación.
- Uso correcto de las bibliotecas estándar de Python (por ejemplo, `csv` para trabajar con archivos separados por comas).
- Claridad y legibilidad del código.
- Funcionalidad y usabilidad de la aplicación.

  ## ⚠️ Sustentación del trabajo

El trabajo debe ser sustentado de manera efectiva, ya que la nota principal se basa en la calidad de la sustentación del código. Asegúrense de que su trabajo sea claro y conciso, y que puedan defender y explicar su código de manera convincente. Recuerden que lo importante no es simplemente entregar un código que funcione correctamente, sino que también sean capaces de sustentar y explicar su lógica y diseño.

**Sustentación del Proyecto**

La sustentación se realizará mediante una conversación con el profesor o con un video de duración aproximada de 8 minutos. El objetivo es presentar una explicación clara y concisa de las funciones del código.

**Lo que se debe hacer:**

- Explicar cómo organizaron el código
• Mostrar el uso de condicionales, bucles y listas
• Demostrar el uso de métodos específicos para manejar cadenas de caracteres o datos separados por comas, etc.

**Lo que no se debe hacer:**

- No explicar cosas obvias
• No se debe explicar el objetivo del reto (el profesor ya lo conoce)
• No se debe explicar detalles innecesarios

## Plazo de entrega

La evaluación se realizará en un plazo de 2 semanas. El ***deadline*** se publicará en repositorio de GitHub.
