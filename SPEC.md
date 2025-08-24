# Especificación técnica — TERROR v0

## Introducción para novatos
**TERROR** es un lenguaje de programación esotérico inspirado en los bolsilibros de terror.  
Su versión inicial (**v0**) está basada en otro esolang muy famoso llamado **Brainfuck** (1993).

👉 ¿Por qué?  
Porque Brainfuck tiene solo **8 instrucciones muy sencillas**, y eso nos permite arrancar un lenguaje funcional desde cero sin complicarnos demasiado.  
Lo que hemos hecho es **mantener esas 8 instrucciones** pero darles nombres de **autores de bolsilibros** y **palabras temáticas de terror**. Así, el código parece un relato pulp, aunque por dentro funcione igual que Brainfuck.

Ejemplo:
- En Brainfuck escribirías:
  ```
  +++.
  ```
  (suma 3 a la celda actual y la imprime como carácter)
- En TERROR escribirías:
  ```
  SILVER KANE SILVER KANE SILVER KANE FRANK CAUDWELL
  ```
  (hace lo mismo, pero con estética bolsilibresca).

De esta forma, cualquier persona que ya sepa Brainfuck entiende TERROR al instante.  
Y si no lo conoces, no pasa nada: aquí tienes la explicación completa.

---

## Modelo de ejecución
- **Memoria**: cinta de bytes (0–255) que puede crecer dinámicamente.
- **Puntero**: empieza en la celda 0.
- **Código**: el intérprete solo reconoce tokens exactos en MAYÚSCULAS; todo lo demás (la prosa pulp) se ignora.

---

## Instrucciones (v0 — “TERROR-8”)
| Token            | Tipo   | Acción                                             |
|------------------|--------|----------------------------------------------------|
| `SILVER KANE`    | Autor  | Incrementa la celda actual (`cell = (cell+1)%256`) |
| `RALPH BARBY`    | Autor  | Decrementa la celda actual (`cell = (cell-1)%256`) |
| `CRIPTA`         | Tema   | Mueve el puntero a la derecha                      |
| `TUMBA`          | Tema   | Mueve el puntero a la izquierda                    |
| `FRANK CAUDWELL` | Autor  | Imprime la celda actual como carácter              |
| `SUSURRO`        | Tema   | Lee un byte de entrada                             |
| `CLARK CARRADOS` | Autor  | Inicio de bucle (`while cell != 0`)                |
| `AMANECER`       | Tema   | Fin de bucle                                       |

---

## Semántica detallada
- **Incremento/Decremento**: los valores van de 0 a 255 y luego vuelven a 0 (operaciones mod 256).
- **Movimiento del puntero**: la cinta puede crecer hacia la derecha o hacia la izquierda si es necesario.
- **Bucle**: si la celda actual es 0 al entrar en `CLARK CARRADOS`, salta tras el `AMANECER` correspondiente.
- **Entrada/Salida**: se trabajan bytes (Latin-1). Entrada por `stdin`, salida por `stdout`.

---

## Relación con Brainfuck
- TERROR v0 es **equivalente a Brainfuck** (1 token TERROR = 1 símbolo de Brainfuck).
- Eso nos permite crear en el futuro un **traductor TERROR → Brainfuck** y usar las herramientas que ya existen para Brainfuck (debuggers, compiladores, optimizadores).
- A partir de v0.1 iremos añadiendo elementos propios (macros, personajes, escenas…) que le darán una personalidad más alejada de Brainfuck.

---

## Roadmap
- **v0.1**: añadir macros llamadas *RITUALES*, saltos con etiquetas (*ESCENAS*) y un modo de depuración `--dump-tape`.
- **v0.2**: variables con nombre (*PERSONAJES*) y un traductor a Brainfuck.