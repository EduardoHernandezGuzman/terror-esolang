# TERROR — esolang bolsilibresco

> Un lenguaje de programación esotérico que mezcla **nombres de autores de bolsilibros** con **palabras temáticas de terror**.  
> El código convive con la prosa pulp: puedes escribir un relato y, entre líneas, esconder instrucciones que el intérprete ejecutará.

---

## ¿Qué es TERROR?
**TERROR** es un lenguaje experimental y esotérico.  
No busca utilidad práctica, sino rendir homenaje a los **bolsilibros españoles de terror** y explorar la programación como un juego creativo.

- El intérprete solo reconoce **tokens en MAYÚSCULAS**.  
- Todo lo demás (narrativa pulp, frases de ambientación, diálogos) se ignora.  
- Así, un programa puede parecer un cuento de terror... pero se ejecuta.

Ejemplo:

```text
En la cripta olvidada, SILVER KANE SILVER KANE FRANK CAUDWELL
```

Esto imprimiría la letra **B** (porque incrementa la celda dos veces y la imprime).

---

## Instalación
Necesitas **Python 3.8+** instalado en tu sistema.

Comprueba tu versión:
```bash
python3 --version
```

Clona el repositorio y entra en la carpeta:

```bash
git clone https://github.com/<tu-usuario>/terror-esolang.git
cd terror-esolang
```

---

## Uso rápido
Ejecuta un programa en TERROR:

```bash
python3 terror.py examples/hola.bolsi
```

Pásale entrada desde la terminal:

```bash
echo "hola" | python3 terror.py examples/eco.bolsi
# o
python3 terror.py examples/eco.bolsi --input "hola"
```

Opciones:
- `--input "texto"` → pasa entrada directamente.  
- `--trace` → muestra la traza de ejecución paso a paso (útil para aprender).  

---

## Tokens de TERROR (v0)
Estos son los 8 comandos básicos del lenguaje:

| Token            | Acción                          | Equivalente BF |
|------------------|---------------------------------|----------------|
| `SILVER KANE`    | Incrementa celda                | `+` |
| `RALPH BARBY`    | Decrementa celda                | `-` |
| `CRIPTA`         | Mueve puntero a la derecha      | `>` |
| `TUMBA`          | Mueve puntero a la izquierda    | `<` |
| `FRANK CAUDWELL` | Imprime celda como carácter     | `.` |
| `SUSURRO`        | Lee un byte de entrada          | `,` |
| `CLARK CARRADOS` | Inicio de bucle (`while != 0`)  | `[` |
| `AMANECER`       | Fin de bucle                    | `]` |

---

## Estructura del repositorio
```
terror-esolang/
├─ README.md
├─ LICENSE
├─ SPEC.md
├─ CONTRIBUTING.md
├─ terror.py
├─ examples/
│  ├─ hola.bolsi
│  └─ eco.bolsi
└─ tests/
   └─ test_hola.py
```

---

## ¿Cómo colaborar?
Consulta [CONTRIBUTING.md](./CONTRIBUTING.md).  
Hay issues marcadas como “good first issue” para empezar fácilmente.

Ideas iniciales:
- Escribir ejemplos narrativos `.bolsi`.  
- Mejorar mensajes de error.  
- Añadir nuevas instrucciones (RITUALES, ESCENAS, PERSONAJES).  
- Crear un traductor TERROR → Brainfuck.  

---

## Licencia
MIT — ver [LICENSE](./LICENSE).