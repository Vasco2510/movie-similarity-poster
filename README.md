# Clustering de Películas Basado en Características Visuales

## Descripción del Proyecto
Este proyecto implementa una solución de aprendizaje no supervisado para agrupar películas utilizando las características visuales extraídas de sus pósteres. La iniciativa busca explorar cómo los patrones estéticos y compositivos en el diseño gráfico de las portadas se relacionan con el género y la temática de los filmes, permitiendo la construcción de un sistema de recomendación basado en similitud visual.

El desarrollo abarca desde la reducción de dimensionalidad de los vectores de características hasta la implementación de una interfaz interactiva para la exploración de clusters y la generación de recomendaciones.

## Metodología
El flujo de trabajo técnico se divide en las siguientes etapas:

1.  **Reducción de Dimensionalidad**: Se aplicaron técnicas de Análisis de Componentes Principales (PCA) y Factorización de Matrices No Negativas (NMF) para gestionar la alta dimensionalidad de los datos visuales, optimizando el costo computacional y la estabilidad de los modelos.
2.  **Clustering**: Se implementaron y compararon algoritmos de agrupamiento:
    * **K-Means++**: Optimizado mediante la selección de centroides iniciales.
    * **Modelos de Mezclas Gaussianas (GMM)**: Utilizando el Criterio de Información Bayesiano (BIC) para la selección óptima de componentes.
3.  **Evaluación**: Uso de métricas como el coeficiente de Silhouette y análisis de distribución para validar la cohesión y separación de los grupos formados.

## Estructura del Repositorio
La arquitectura del proyecto sigue un diseño modular para facilitar el mantenimiento y la escalabilidad:

* `app.py`: Punto de entrada de la aplicación Streamlit.
* `data/`: Módulos para la carga de datasets y la integración de archivos de clusters (.pkl).
* `logic/`: Implementación del motor de recomendación y lógica de similitud.
* `ui/`: Componentes de la interfaz de usuario y visualización de pósteres.
* `config/`: Parámetros de configuración del sistema.
* `utils/`: Funciones auxiliares de procesamiento.
* `requirements.txt`: Especificación de dependencias del entorno.

## Requisitos del Sistema
El proyecto requiere Python 3.x y las siguientes librerías principales:
* Streamlit (Interfaz de usuario)
* Pandas (Gestión de datos)
* Scikit-learn (Algoritmos de ML y preprocesamiento)
* Numpy (Operaciones matriciales)

## Para iniciar el proyecto
Ejecutar `streamlit run app.py` en la terminal

Para instalar las dependencias, ejecute:
```bash
pip install -r requirements.txt
```
##Características de la Interfaz
 La aplicación permite al usuario:

- Seleccionar entre diferentes combinaciones de algoritmos (GMM, K-Means++) y métodos de reducción (PCA, NMF).

- Explorar películas por clusters en entornos de 2D y 3D.

- Visualizar información detallada y pósteres de películas seleccionadas.

- Obtener recomendaciones de películas similares dentro del mismo cluster, con opción de filtrado por género.

