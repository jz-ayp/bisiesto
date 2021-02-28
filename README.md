# `Nombre del tema`

## Ejercicio: `<Título del ejercicio>`

## Objetivos
- Formular una solución efectiva a un problema que incorpora `<recursion>, <user-defined functions>, <iteration>, <conditionals>`.
- Interpretar adecuadamente los requisitos de solución de un problema a partir de su descripcion en lenguaje natural.
- Generar, a partir del análisis del problema:
    - La identificación correcta de las entradas y salidas requeridas, y
    - Una explicación, a grandes rasgos, del proceso de solución.
- Elaborar un diagrama de flujo que muestre la lógica del algoritmo.
- Codificar el algoritmo en un programa correcto de Python.
- Identificar y ejecutar los casos de prueba pertinentes y suficientes para verificar la funcionalidad de la solución propuesta.

- `Recognize, Identify, Select, Analyze, Differentiate, Distinguish, Diagram, Examine, Outline, Subdivide, Understand, Demonstrate, Illustrate, Represent, Interpret, Evaluate, Apply, Assess, Chart, Construct, Develop, Implement, Prepare, Provide, Compute, Contribute, Determine, Establish, Include, Produce, Show, Combine, Design, Make, Plan, Compose, Create, Devise, Formulate, `

## Instrucciones
- Elabora el análisis y el algoritmo ***antes de escribir el código***. Utiliza un diagrama de flujo para representar tu algoritmo e ilustrar su lógica.
    - [diagrams.net](https://app.diagrams.net/) es una herramienta gratuita y fácil de usar con la que puedes crear diagramas de flujo. 
    - Puedes ver un ejemplo de como subir diagramas de flujo a GitHub [aquí](https://youtu.be/oy5nhA7QpNI).

- **Diseña un programa para `<...>`**.

- Codifica tu solución en el archivo [`main.py`](/main.py).
   
- Utiliza los siguientes ejemplos para dar formato a tus entradas y salidas `<user prompt> <output> <file>`:
  ```
  <format example>
  ```
  
- Prueba tu programa corriéndolo varias veces con diferentes entradas. Verifica que tu algoritmo produzca las salidas correctas. Pon atención especial a los casos que pudieran ser problemáticos de manejar (casos límite).

- Añade la siguiente cadena de documentación (*docstring*) al inicio de tu programa:
  ```
  '''
  Tarea: <Nombre de la tarea y del ejercicio>
  Author: <Tu nombre>
  Fecha de entrega: DD/MM/YYYY
  Grupo: ESI-XXXX-XX
  Profesor: XXX

  Descripción:
  <Una breve descripción del programa>
  '''
  ```
  
## Entrega
1. Completa este y el resto de los ejercicios y compila, para cada ejercicio, el enunciado, análisis, diagrama de flujo y código, en un informe tal como se describe en los [requisitos para entrega de tareas](https://canvas.iteso.mx/courses/12856/modules/items/418369) en Canvas. También los puedes consultar [aquí](/report/report_example.pdf). No olvides incluir portada y conclusiones.

`1. Complete and submit your program as outlined in this [instructional video](https://youtu.be/SrJ_c8S1_D8).`

2. Agrega el diagrama de flujo a la carpeta [`flowchart`](/flowchart) (puedes ver un [ejemplo de cómo se hace](https://youtu.be/oy5nhA7QpNI)).

3. Agrega el informe en PDF a la carpeta [`report`](/report).

## Casos de prueba de ejemplo
| Entradas | Salidas |
|:---------|:--------|
| `entrada11`<br>`entrada12` | `salida11`<br>`salida12`<br>`salida13` |
| `entrada21` | `salida21`<br>`salida22` |
| `entrada31`<br>`entrada32`<br>`entrada33`  | `salida21`<br>`salida22` |

## Rúbrica
Verifica tu entrega contra esta rúbrica para maximizar tu calificación. Los puntos se indican en porcentaje.

| Criterio | Puntos |
|----------|--------|
| Entrega:<br>Todos los archivos fueron entregados tal como se indicó, vía GitHub y Canvas.<br>El informe:<br>- tiene portada con todos los datos requeridos,<br>- en formato PDF,<br>- las conclusiones incluyen los elementos indicados en el documento de requerimientos. | 5 |
| Seudocódigo:<br>- incluido como texto en el informe, no como captura de pantalla,<br>- el indentado es correcto.<br>Código:<br>- incluido como texto en el informe, no como captura de pantalla,<br>- con tipo de letra de ancho fijo,<br>- espaciado sencillo,<br>- sin líneas que alcancen el margen. | 5 |
| Análisis:<br>- identifica todas las entradas y salidas necesarias,<br>- no clasifica como entrada una salida o viceversa,<br>- no nombra entradas o salidas innecesarias.<br>- El proceso es claro,<br>- no es una simple repetición del enunciado,<br>- sino un acercamiento a la solución, y<br>- no incluye seudocódigo. | 15 |
| *Docstring*:<br>- presente en la parte superior del programa, <br>- tiene el formato exacto indicado en las instrucciones, y<br>- su contenido fue editado por el estudiante.<br>Comentarios:<br>- hay comentarios en el programa,<br>- describen claramente el propósito del código, y<br>- siguen los lineamientos del PEP8<br>[PEP8 Comments](https://www.python.org/dev/peps/pep-0008/#comments) | 5 |
| Identificadores:<br>- usan [snake case](https://en.wikipedia.org/wiki/Snake_case), y<br>- son descriptivos del dato que representan.<br>[PEP8 Naming Conventions](https://www.python.org/dev/peps/pep-0008/#naming-conventions) | 5 |
| Formato de salidas:<br>- conforme al ejemplo en las instrucciones. | 5 |
| Diagrama de flujo:<br>- es claro y legible,<br>- corresponde con la lógica del programa,<br>- usa las formas geométricas correctas, y<br>- está en formato png<br>[Cómo subir diagramas de flujo a GitHub](https://youtu.be/oy5nhA7QpNI) | 15 |
| Pruebas de ejecución:<br>- son suficientes para comprobar la funcionalidad del programa,<br>- al menos una de las capturas de pantalla muestra el escritorio completo, y<br>- son legibles. | 15 |
| Funcionalidad:<br>- pasa los casos de prueba de ejemplo, y<br>- pasa los casos de prueba reservados por el profesor. | 30 |

Estos puntajes son equivalentes, aproximadamente, a la siguiente ponderación:
- Presentación: 20%
- Funcionalidad: 60%
- Pruebas: 20%
