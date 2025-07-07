## Problemática y Motivacion

En el ámbito educativo, particularmente en los niveles escolares y en los primeros ciclos universitarios de carreras vinculadas a la computación, la enseñanza de algoritmos representa un desafío constante. Los estudiantes, al encontrarse por primera vez con conceptos como variables, estructuras de control, condicionales, ciclos e incluso funciones, deben desarrollar simultáneamente habilidades de abstracción, lógica y sintaxis.

Sin embargo, uno de los obstáculos más recurrentes es la ausencia de un lenguaje estándar y estructurado para expresar algoritmos. En muchos cursos se emplea pseudocódigo de forma libre o con formatos diversos, lo que introduce ambigüedad, inconsistencia y, a menudo, errores de interpretación tanto para estudiantes como para docentes. La informalidad en la escritura de algoritmos termina dificultando el objetivo principal del curso: desarrollar el pensamiento lógico.

Además, en un entorno donde se promueve el aprendizaje autónomo, la falta de herramientas que validen automáticamente lo que el estudiante escribe genera una barrera en la retroalimentación inmediata, que es crucial para el aprendizaje activo. Un estudiante que comete un error sintáctico o semántico en un algoritmo puede tardar en recibir corrección o nunca detectar el error, afectando su confianza y progreso.

Por otra parte, desde la perspectiva docente, no contar con un sistema que permita validar de forma automática la estructura lógica de los algoritmos representa una carga adicional de trabajo y limita la posibilidad de escalar el aprendizaje en entornos masivos o virtuales.

En este contexto, se hace evidente la necesidad de una solución que combine claridad, formalidad, validación automática y adaptabilidad pedagógica.

## Objetivo

Este proyecto tiene como objetivo principal el diseño e implementación de un lenguaje de programación educativo específico para la descripción de algoritmos básicos, orientado a facilitar el proceso de enseñanza-aprendizaje de la lógica computacional en entornos académicos. Este lenguaje se implementa a través de un compilador desarrollado con ANTLR4 y ejecutado en Python, y está concebido como una herramienta educativa que combine rigor sintáctico con facilidad de uso.

Diseñar una gramática formal clara, comprensible y extensible que represente las construcciones más comunes en algoritmos básicos: lectura de datos, impresión, asignaciones, expresiones aritméticas, condicionales (si/sino) y ciclos (mientras).

Implementar un compilador funcional que permita analizar, validar y recorrer árboles de sintaxis a partir de los programas escritos en este lenguaje.

Desarrollar una interfaz de análisis que genere pseudocódigo estructurado como salida, permitiendo a los estudiantes visualizar y entender cómo se traduce su lógica en una forma legible y ordenada.

Sentar las bases para una futura expansión del compilador hacia la ejecución directa, la generación de código Python o la integración en plataformas educativas como Moodle o Jupyter Notebooks.

Promover el uso de tecnologías de código abierto y lenguajes accesibles para reducir las barreras de entrada y fomentar la participación de más instituciones educativas en la mejora continua del lenguaje.

## Conclusiones

El desarrollo de este proyecto individual ha permitido consolidar competencias técnicas, metodológicas y formativas en el campo de los compiladores y del diseño de lenguajes específicos. A través del diseño e implementación de un lenguaje de programación educativo utilizando ANTLR4 y Python, se logró no solo abordar una problemática concreta del ámbito educativo, sino también proponer una solución funcional, extensible y con alto valor pedagógico.

Una de las principales conclusiones es que el desarrollo de un compilador va más allá del procesamiento técnico del código fuente: implica comprender el contexto de uso del lenguaje, anticipar los errores comunes de los usuarios, y diseñar herramientas que comuniquen resultados de forma clara, útil y estructurada. Esta perspectiva llevó a implementar una gramática robusta que soporta estructuras esenciales como lectura, impresión, condicionales y ciclos, así como a integrar un generador de pseudocódigo estructurado que actúa como puente entre el lenguaje diseñado y su interpretación lógica.