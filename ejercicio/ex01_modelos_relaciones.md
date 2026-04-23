# Ejercicios 1. Identificar modelos y relaciones
#### Tema: Academia online

#### 1. Que aprender
- Identificar en modelo que contiene la entidad principal
- Identificar el modelo que contiene la actividad o interaccion. 
- Entender como se relacionan ambos modelos

#### Este razonamiento es la base de la practica
- primero indentificas los datos
- consultas con ORM
- despues agregas los muestras y los exportas

#### 2. Analisis del caso
La academia quiere saber:
- cuantas tutorias ha recibido cada alumno 

De este frase salen dos preguntas
¿Sobre quien queremos resumir la informacion?
Sobre el alumno

¿Que evento o interaccion queremos contar?
Las Tutorias

Por lo tanto:
- academy.student = modelo principal
- academy.tutoring = modelo de actividad o detalle

#### 3. Identificacion de modelos
### Modelo principal
Representa al alumno

Es el modelo desde el que tiene sentido resumir informacion como:

- nombre
- email
- numero total de tutorias
- ultima tutoria
- estado academico

### Modelo de actividad: `academy.tutoring`

Representa cada tutoria realizada o registrada

Cada registro de este modelo representa una interaccion concreta:

- 

