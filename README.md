# Mi Primer Proyecto en Python

## 📁 Estructura del proyecto

```
mi_primer_proyecto/
├── fase1_python/         → Python desde cero
├── fase2_machine_learning/  → Machine Learning con scikit-learn
└── fase3_llms/           → LLMs, Prompt Engineering y RAG
```

---

## 🐍 FASE 1 — Python desde cero

### 🏧 cajero.py
Un cajero automático creado con Python desde cero.

**¿Qué hace?**
- Ver saldo
- Ingresar dinero
- Retirar dinero
- Guarda el saldo aunque cierres el programa

### 🌤️ tiempo.py
Programa que consulta el tiempo real de **Cádiz** usando una API.

**¿Qué muestra?**
- Temperatura actual
- Humedad
- Lluvia
- Viento

### 🌍 buscador_tiempo.py
Programa que consulta el tiempo de **cualquier ciudad del mundo** usando varias APIs.

**¿Qué muestra?**
- Temperatura actual
- Humedad
- Lluvia
- Viento

### 🗄️ base_de_datos.py
Introducción a bases de datos con SQLite.

### 🏋️ Ejercicios de Práctica

#### ejercicio1.py
Gestión de productos con diccionarios, bucles y condicionales.

#### ejercicio2.py
Funciones para calcular media, número mayor y menor de una lista.

#### ejercicio3.py
Bucles con input del usuario para clasificar números pares e impares.

#### ejercicio4.py
Gestión de notas con archivos, lectura y cálculo de media.

#### ejercicio5.py
Agenda de contactos completa con menú interactivo y guardado en archivo.

---

## 🤖 FASE 2 — Machine Learning con scikit-learn

### 📊 intro_pandas.py
Introducción a pandas: creación de DataFrames, acceso a datos, filtros y modificaciones.

### 🧹 limpieza.py
Limpieza de datos con pandas: valores vacíos, relleno y eliminación de duplicados.

### 📈 groupby.py
Agrupación y resumen de datos con groupby y estadísticas básicas.

### 📉 graficos.py
Visualización de datos con matplotlib: gráficos de barras, líneas y tarta.

### 🎓 analisis_notas.py
Proyecto completo de análisis de notas con pandas y matplotlib.

**¿Qué hace?**
- Crea una tabla con asignaturas, notas y profesores
- Calcula media, nota más alta y más baja
- Filtra asignaturas aprobadas
- Muestra un gráfico de barras

### 🤖 mi_primer_modelo.py
Primer modelo de Machine Learning: regresión lineal para predecir precios de casas.

**¿Qué hace?**
- Predice el precio de una casa según su tamaño y número de habitaciones
- Visualiza los datos reales vs la predicción del modelo

### 🎯 clasificacion.py
Modelo de clasificación con KNN para predecir si un estudiante aprobará o suspenderá.

### 🌸 iris.py
Clasificación con el famoso dataset Iris: identifica especies de flores por sus medidas.

**¿Qué hace?**
- Entrena un modelo con 120 flores reales
- Lo evalúa con 30 flores que nunca ha visto
- Muestra la matriz de confusión y el informe de clasificación

### 📐 normalizacion.py
Normalización de datos con MinMaxScaler para escalar todas las columnas entre 0 y 1.

### 📉 overfitting.py
Demostración de overfitting y underfitting comparando modelos con k=1 y k=5.

### 🌳 arbol.py
Árbol de decisión para clasificar especies de flores con visualización gráfica del árbol.

### 🌲 random_forest.py
Random Forest con 100 árboles comparado con un árbol individual, incluyendo análisis de importancia de características.

### 🏆 proyecto_estudiantes.py
Proyecto completo de Machine Learning: predictor de resultados académicos.

**¿Qué hace?**
- Analiza datos de 20 estudiantes
- Normaliza los datos automáticamente
- Entrena y compara 3 modelos: KNN, Árbol de decisión y Random Forest
- Visualiza la comparación de modelos en un gráfico
- Predice si un estudiante nuevo aprobará o suspenderá

### 🚢 titanic.py
Proyecto de Machine Learning con datos reales: predicción de supervivencia en el Titanic.

**¿Qué hace?**
- Carga y limpia el dataset real del Titanic (891 pasajeros)
- Rellena valores vacíos y convierte datos de texto a números
- Entrena y compara 3 modelos: KNN (78%), Árbol de decisión (76%) y Random Forest (76%)
- Analiza qué características fueron más importantes para sobrevivir
- Descubre que el precio del billete, el género y la edad fueron los factores clave

### 📊 regresion_logistica.py
Modelo de regresión logística con predicción de probabilidades.

### 🔄 cross_validation.py
Evaluación de modelos con cross-validation de 5 partes.

### 🔍 hiperparametros.py
Búsqueda automática de la mejor configuración con GridSearchCV.

### 🎨 seaborn_viz.py
Visualizaciones profesionales con seaborn.

### 🏥 diabetes.py
Proyecto de Machine Learning con dataset real de diabetes (768 pacientes).

**¿Qué hace?**
- Analiza datos médicos reales de pacientes
- Compara 3 modelos con cross-validation
- Descubre que la glucosa es el factor más importante para predecir diabetes
- Visualiza la importancia de cada característica con seaborn

---

## 🧠 FASE 3 — LLMs, Agentes IA y RAG

### 🤖 mi_primer_llm.py
Primera llamada a un LLM real desde Python usando la API de Groq y el modelo LLaMA 3.3.

**¿Qué hace?**
- Conecta con la API de Groq de forma segura usando .env
- Envía una pregunta al modelo y muestra la respuesta
- Introduce los conceptos de tokens, temperature y max_tokens

### ✍️ prompt_engineering.py
Técnicas de Prompt Engineering para obtener mejores respuestas de un LLM.

**Técnicas aplicadas:**
- Prompts específicos vs vagos
- Roles con system prompt
- Formato estructurado
- Few-shot prompting
- Chain of Thought

### 🛡️ prompt_avanzado.py
Prompt Engineering avanzado con técnicas profesionales.

**¿Qué hace?**
- Prompts negativos para acotar respuestas
- Respuestas en JSON procesadas con Python
- Protección contra prompt injection

### 💬 conversacion.py
Chat con memoria usando historial de mensajes.

**¿Qué hace?**
- Mantiene el contexto de la conversación
- Demuestra cómo los LLMs construyen la memoria con el historial

### 🖥️ chat_interactivo.py
Chat interactivo en tiempo real desde la terminal con streaming.

**¿Qué hace?**
- Conversación fluida desde la terminal
- Respuestas en tiempo real palabra a palabra
- Escribe 'salir' para terminar

### 🧠 memoria_avanzada.py
Tres soluciones avanzadas para gestionar la memoria en conversaciones largas.

**Soluciones implementadas:**
- Limitar el historial a los últimos N mensajes
- Resumir automáticamente cuando el historial crece demasiado
- Guardar el historial en archivo JSON para persistencia entre sesiones

### 🔢 embeddings.py
Generación y comparación de embeddings con la API de Google Gemini.

**¿Qué hace?**
- Convierte texto en vectores numéricos de 3072 dimensiones
- Calcula similitud coseno entre textos
- Demuestra búsqueda semántica por significado

### 🗄️ chromadb_intro.py
Búsqueda semántica con FAISS como base de datos vectorial.

**¿Qué hace?**
- Genera embeddings de 8 recetas y los guarda en FAISS
- Busca las 3 recetas más relevantes para cualquier consulta
- Demuestra búsqueda por distancia L2

### 🏋️ Ejercicios de Práctica Fase 3

#### ejercicio_prompt.py
Asistente de profesor de idiomas con rol, formato estructurado y prompts negativos.

#### ejercicios_memoria.py
Agente de viajes con memoria persistente en archivo JSON y streaming en tiempo real.

#### ejercicios_embeddings.py
Buscador semántico de recetas que devuelve las 3 más relevantes para cualquier consulta.

---

## ¿Qué he aprendido?

### 🐍 Python y fundamentos
- Variables y tipos de datos
- Funciones, bucles y condicionales
- Archivos y manejo de errores
- Listas y diccionarios
- APIs
- Bases de datos con SQLite
- Git y GitHub
- Visual Studio Code

### 🤖 Machine Learning
- Análisis de datos con pandas
- Visualización con matplotlib y seaborn
- Regresión lineal y logística
- Clasificación con KNN
- Árboles de decisión y Random Forest
- Train/Test Split y Cross-validation
- Normalización de datos
- Matriz de confusión
- GridSearchCV para hiperparámetros
- Datasets reales: Iris, Titanic y Diabetes

### 🧠 LLMs e Inteligencia Artificial
- Qué son los LLMs, tokens, embeddings y transformers
- Llamadas a APIs de LLMs (Groq, Google Gemini)
- Prompt Engineering (8 técnicas)
- Protección contra prompt injection
- Conversaciones con memoria e historial
- Streaming en tiempo real
- Embeddings y similitud semántica
- Búsqueda semántica con FAISS
- Bases de datos vectoriales

---

## Autora
Gala Chacón